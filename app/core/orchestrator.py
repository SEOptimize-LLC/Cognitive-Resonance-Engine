"""
Research Orchestrator Module
============================
Coordinates the entire research pipeline, sequencing all analysis modules
and aggregating results into the final ResearchResults object.
"""

import json
import logging
from typing import Callable, Optional, Dict, Any, List

from app.config import (
    PERPLEXITY_RESEARCH_MODEL,
    PIPELINE_STAGES,
    APP_CONFIG
)
from app.models.research_models import (
    ClientInput,
    ResearchResults,
    CompanyProfile,
    ICP,
    ValuePropositionCanvas,
    PainPointTaxonomy,
    CustomerJourneyMap,
    ICPAnalysisResult
)
from app.llm.openrouter_client import OpenRouterClient, CostTracker

# Import analysis modules
from app.core.data_ingestion import DataIngestionModule
from app.core.audience_research import AudienceResearchModule
from app.core.usp_extraction import USPExtractionModule
from app.core.pain_taxonomy import PainTaxonomyModule
from app.core.journey_mapping import JourneyMappingModule


logger = logging.getLogger(__name__)


# Type alias for progress callback
ProgressCallback = Callable[[str, str, Optional[Any], Optional[str]], None]


class ResearchOrchestrator:
    """
    Main orchestrator that coordinates the entire research pipeline.
    
    The pipeline follows this sequence:
    1. Data Ingestion - Gather information about the client via Perplexity
    2. Audience Research - Generate ICPs from gathered data
    3. USP Extraction - Map value propositions for each ICP
    4. Pain Taxonomy - Deep pain point analysis for each ICP
    5. Journey Mapping - Create customer journey maps for each ICP
    """
    
    def __init__(
        self,
        analysis_model: str,
        cost_tracker: Optional[CostTracker] = None
    ):
        """
        Initialize the orchestrator.
        
        Args:
            analysis_model: The model ID to use for analysis tasks
            cost_tracker: Optional cost tracker for token usage
        """
        self.analysis_model = analysis_model
        self.cost_tracker = cost_tracker or CostTracker()
        
        # Initialize the LLM client
        self.llm_client = OpenRouterClient(
            cost_tracker=self.cost_tracker
        )
        
        # Initialize analysis modules
        self.data_ingestion = DataIngestionModule(
            llm_client=self.llm_client,
            research_model=PERPLEXITY_RESEARCH_MODEL
        )
        
        self.audience_research = AudienceResearchModule(
            llm_client=self.llm_client,
            analysis_model=analysis_model
        )
        
        self.usp_extraction = USPExtractionModule(
            llm_client=self.llm_client,
            analysis_model=analysis_model
        )
        
        self.pain_taxonomy = PainTaxonomyModule(
            llm_client=self.llm_client,
            analysis_model=analysis_model
        )
        
        self.journey_mapping = JourneyMappingModule(
            llm_client=self.llm_client,
            analysis_model=analysis_model
        )
    
    def run_research(
        self,
        client_input: ClientInput,
        progress_callback: Optional[ProgressCallback] = None
    ) -> ResearchResults:
        """
        Execute the full research pipeline.
        
        Args:
            client_input: The client information to research
            progress_callback: Optional callback for progress updates
                Signature: (stage_id, status, data, error) -> None
                
        Returns:
            ResearchResults containing all analysis outputs
        """
        
        def update_progress(
            stage_id: str,
            status: str,
            data: Any = None,
            error: str = None
        ):
            """Helper to update progress if callback provided."""
            if progress_callback:
                progress_callback(stage_id, status, data, error)
            
            # Log progress
            if status == "running":
                logger.info(f"Starting stage: {stage_id}")
            elif status == "complete":
                logger.info(f"Completed stage: {stage_id}")
            elif status == "error":
                logger.error(f"Error in stage {stage_id}: {error}")
        
        # Initialize result containers
        company_profile: Optional[CompanyProfile] = None
        icps: List[ICP] = []
        icp_results: List[ICPAnalysisResult] = []
        raw_research_data: Dict[str, Any] = {}
        
        try:
            # ===== Stage 1: Data Ingestion =====
            update_progress("data_ingestion", "running")
            
            try:
                company_profile, raw_research_data = \
                    self.data_ingestion.run(client_input)
                update_progress(
                    "data_ingestion",
                    "complete",
                    data={"company": company_profile.name}
                )
            except Exception as e:
                update_progress("data_ingestion", "error", error=str(e))
                raise
            
            # ===== Stage 2: Audience Research (ICP Generation) =====
            update_progress("audience_research", "running")
            
            try:
                icps = self.audience_research.run(
                    client_input=client_input,
                    company_profile=company_profile,
                    raw_research=raw_research_data,
                    num_icps=client_input.num_icps
                )
                update_progress(
                    "audience_research",
                    "complete",
                    data={"num_icps": len(icps)}
                )
            except Exception as e:
                update_progress("audience_research", "error", error=str(e))
                raise
            
            # ===== Stages 3-5: Per-ICP Analysis =====
            for i, icp in enumerate(icps):
                icp_result = ICPAnalysisResult(icp=icp)
                
                # Stage 3: USP Extraction
                stage_id = f"usp_extraction_{i+1}"
                update_progress(stage_id, "running")
                
                try:
                    vp_canvas = self.usp_extraction.run(
                        client_input=client_input,
                        company_profile=company_profile,
                        icp=icp
                    )
                    icp_result.value_proposition = vp_canvas
                    update_progress(
                        stage_id,
                        "complete",
                        data={"fit_score": vp_canvas.fit_score}
                    )
                except Exception as e:
                    update_progress(stage_id, "error", error=str(e))
                    logger.warning(
                        f"USP extraction failed for ICP {i+1}: {e}"
                    )
                
                # Stage 4: Pain Taxonomy
                stage_id = f"pain_taxonomy_{i+1}"
                update_progress(stage_id, "running")
                
                try:
                    pain_tax = self.pain_taxonomy.run(
                        client_input=client_input,
                        company_profile=company_profile,
                        icp=icp
                    )
                    icp_result.pain_taxonomy = pain_tax
                    update_progress(
                        stage_id,
                        "complete",
                        data={
                            "num_pains": (
                                len(pain_tax.functional_pains) +
                                len(pain_tax.financial_pains) +
                                len(pain_tax.emotional_pains)
                            )
                        }
                    )
                except Exception as e:
                    update_progress(stage_id, "error", error=str(e))
                    logger.warning(
                        f"Pain taxonomy failed for ICP {i+1}: {e}"
                    )
                
                # Stage 5: Journey Mapping
                stage_id = f"journey_mapping_{i+1}"
                update_progress(stage_id, "running")
                
                try:
                    journey = self.journey_mapping.run(
                        client_input=client_input,
                        company_profile=company_profile,
                        icp=icp,
                        value_proposition=icp_result.value_proposition,
                        pain_taxonomy=icp_result.pain_taxonomy
                    )
                    icp_result.journey_map = journey
                    update_progress(
                        stage_id,
                        "complete",
                        data={"stages": 5}
                    )
                except Exception as e:
                    update_progress(stage_id, "error", error=str(e))
                    logger.warning(
                        f"Journey mapping failed for ICP {i+1}: {e}"
                    )
                
                icp_results.append(icp_result)
            
            # ===== Compile Final Results =====
            results = ResearchResults(
                client_input=client_input,
                company_profile=company_profile,
                icps=icp_results,
                raw_research_data=raw_research_data,
                cost_summary=self.cost_tracker.get_summary()
            )
            
            logger.info(
                f"Research complete. Total cost: "
                f"${results.cost_summary.get('total_cost', 0):.4f}"
            )
            
            return results
            
        except Exception as e:
            logger.exception(f"Research pipeline failed: {e}")
            
            # Return partial results if available
            return ResearchResults(
                client_input=client_input,
                company_profile=company_profile,
                icps=icp_results,
                raw_research_data=raw_research_data,
                cost_summary=self.cost_tracker.get_summary(),
                error=str(e)
            )
    
    def run_stage(
        self,
        stage_id: str,
        client_input: ClientInput,
        **kwargs
    ) -> Any:
        """
        Run a single stage of the pipeline.
        
        Useful for re-running specific stages or debugging.
        
        Args:
            stage_id: The stage identifier
            client_input: The client information
            **kwargs: Additional arguments for the stage
            
        Returns:
            The output of the requested stage
        """
        stage_methods = {
            "data_ingestion": lambda: self.data_ingestion.run(client_input),
            "audience_research": lambda: self.audience_research.run(
                client_input=client_input,
                company_profile=kwargs.get("company_profile"),
                raw_research=kwargs.get("raw_research"),
                num_icps=client_input.num_icps
            ),
            "usp_extraction": lambda: self.usp_extraction.run(
                client_input=client_input,
                company_profile=kwargs.get("company_profile"),
                icp=kwargs.get("icp")
            ),
            "pain_taxonomy": lambda: self.pain_taxonomy.run(
                client_input=client_input,
                company_profile=kwargs.get("company_profile"),
                icp=kwargs.get("icp")
            ),
            "journey_mapping": lambda: self.journey_mapping.run(
                client_input=client_input,
                company_profile=kwargs.get("company_profile"),
                icp=kwargs.get("icp"),
                value_proposition=kwargs.get("value_proposition"),
                pain_taxonomy=kwargs.get("pain_taxonomy")
            )
        }
        
        if stage_id not in stage_methods:
            raise ValueError(f"Unknown stage: {stage_id}")
        
        return stage_methods[stage_id]()