"""
USP Extraction Module
=====================
Maps value propositions to each ICP using the Value Proposition Canvas
framework, identifying pain relievers and gain creators.
"""

import json
import logging
from typing import Dict, Any, List

from app.models.research_models import (
    ClientInput,
    CompanyProfile,
    ICP,
    ValuePropositionCanvas,
    PainReliever,
    GainCreator
)
from app.llm.openrouter_client import OpenRouterClient


logger = logging.getLogger(__name__)


VPC_ANALYSIS_PROMPT = """
You are an expert strategist specializing in the Value Proposition Canvas
framework by Alexander Osterwalder. Your task is to create a precise
product-market fit analysis.

## Company Information

**Company:** {company_name}
**Industry:** {industry}

**Products/Services:**
{products_services}

**Stated Value Propositions:**
{value_propositions}

## Target ICP Profile

**ICP Name:** {icp_name}
**Description:** {icp_description}

**Demographics:**
{demographics}

**Psychographics:**
{psychographics}

**Key Motivations:**
{motivations}

**Key Pain Points:**
{pain_points}

## Your Task

Create a comprehensive Value Proposition Canvas analysis that maps the
company's offerings to this specific ICP's needs.

### Customer Profile (Right Side of Canvas)

1. **Customer Jobs** - What is this ICP trying to get done?
   - Functional jobs (tasks, problems to solve)
   - Social jobs (look good, gain power/status)
   - Emotional jobs (feel secure, confident, successful)

2. **Pains** - What annoys them before, during, and after the job?
   - Obstacles and risks
   - Undesired outcomes
   - Negative emotions

3. **Gains** - What outcomes and benefits do they want?
   - Required gains (must have)
   - Expected gains (should have)
   - Desired gains (want to have)
   - Unexpected gains (delighters)

### Value Map (Left Side of Canvas)

4. **Products/Services** - What offerings address their jobs?

5. **Pain Relievers** - How do the products eliminate or reduce pains?
   - Specific feature → Specific pain addressed
   - How significant is the relief?

6. **Gain Creators** - How do the products create gains?
   - Specific feature → Specific gain created
   - How significant is the gain?

### Fit Analysis

7. **Value Proposition Statement**
   A clear statement of why this ICP should choose this solution.

8. **Fit Score** (0-100)
   How well does the value proposition match this ICP's needs?

9. **Unique Differentiators**
   What makes this offering unique for this specific ICP?

10. **Gaps and Weaknesses**
    Where does the value proposition fall short?

## Output Format

```json
{{
    "customer_jobs": {{
        "functional": ["Job 1", "Job 2"],
        "social": ["Job 1", "Job 2"],
        "emotional": ["Job 1", "Job 2"]
    }},
    "customer_pains": [
        {{
            "pain": "Description of pain",
            "severity": 8,
            "category": "obstacle|risk|negative_outcome|negative_emotion"
        }}
    ],
    "customer_gains": [
        {{
            "gain": "Description of gain",
            "importance": 9,
            "type": "required|expected|desired|unexpected"
        }}
    ],
    "products_services_fit": [
        {{
            "product": "Product name",
            "jobs_addressed": ["Job 1", "Job 2"],
            "relevance_score": 8
        }}
    ],
    "pain_relievers": [
        {{
            "pain_addressed": "The specific pain being addressed",
            "feature_or_capability": "The feature that addresses it",
            "how_relieved": "Explanation of how it relieves the pain",
            "relief_significance": 9
        }}
    ],
    "gain_creators": [
        {{
            "gain_created": "The specific gain being created",
            "feature_or_capability": "The feature that creates it",
            "how_created": "Explanation of how it creates the gain",
            "creation_significance": 8
        }}
    ],
    "value_proposition_statement": "For [ICP] who [situation], [Product] is a [category] that [key benefit]. Unlike [alternatives], we [key differentiator].",
    "fit_score": 85,
    "unique_differentiators": [
        "Differentiator 1",
        "Differentiator 2"
    ],
    "gaps_weaknesses": [
        "Gap 1",
        "Gap 2"
    ],
    "messaging_recommendations": [
        "Lead with X because...",
        "Emphasize Y for this audience..."
    ]
}}
```

Analyze now:
"""


class USPExtractionModule:
    """
    Creates Value Proposition Canvas analysis for each ICP.
    """
    
    def __init__(
        self,
        llm_client: OpenRouterClient,
        analysis_model: str
    ):
        """
        Initialize the USP extraction module.
        
        Args:
            llm_client: The OpenRouter client for API calls
            analysis_model: The model ID for analysis tasks
        """
        self.llm_client = llm_client
        self.analysis_model = analysis_model
    
    def run(
        self,
        client_input: ClientInput,
        company_profile: CompanyProfile,
        icp: ICP
    ) -> ValuePropositionCanvas:
        """
        Generate Value Proposition Canvas for the given ICP.
        
        Args:
            client_input: Original client input
            company_profile: Parsed company profile
            icp: The ICP to analyze
            
        Returns:
            ValuePropositionCanvas object
        """
        logger.info(
            f"Creating VPC for ICP: {icp.icp_name}"
        )
        
        # Format products/services
        products_list = []
        for ps in company_profile.products_services:
            features = ", ".join(ps.features[:5]) if ps.features else "N/A"
            products_list.append(
                f"- **{ps.name}**: {ps.description}\n"
                f"  Features: {features}"
            )
        products_str = "\n".join(products_list) or "Not specified"
        
        # Format value propositions
        vp_list = company_profile.stated_value_propositions or []
        vp_str = "\n".join(f"- {vp}" for vp in vp_list) or "Not specified"
        
        # Format demographics
        demo = icp.demographics
        demo_parts = []
        if demo.company_size:
            demo_parts.append(f"Company Size: {demo.company_size}")
        if demo.job_titles:
            demo_parts.append(f"Job Titles: {', '.join(demo.job_titles)}")
        if demo.industry_verticals:
            demo_parts.append(
                f"Industries: {', '.join(demo.industry_verticals)}"
            )
        if demo.budget_range:
            demo_parts.append(f"Budget: {demo.budget_range}")
        demo_str = "\n".join(f"- {d}" for d in demo_parts) or "Not specified"
        
        # Format psychographics
        psycho = icp.psychographics
        psycho_parts = [
            f"Decision Style: {psycho.decision_style.value}",
            f"Risk Tolerance: {psycho.risk_tolerance.value}"
        ]
        if psycho.core_values:
            psycho_parts.append(f"Values: {', '.join(psycho.core_values)}")
        if psycho.fears:
            psycho_parts.append(f"Fears: {', '.join(psycho.fears)}")
        if psycho.aspirations:
            psycho_parts.append(f"Aspirations: {', '.join(psycho.aspirations)}")
        psycho_str = "\n".join(f"- {p}" for p in psycho_parts)
        
        # Format motivations
        motivations_list = [
            f"- {m.statement} (Intensity: {m.intensity}/10)"
            for m in icp.motivations[:7]
        ]
        motivations_str = "\n".join(motivations_list) or "Not specified"
        
        # Format pain points
        pains_list = [
            f"- {p.statement} (Severity: {p.severity}/10)"
            for p in icp.pain_points[:7]
        ]
        pains_str = "\n".join(pains_list) or "Not specified"
        
        # Build the prompt
        prompt = VPC_ANALYSIS_PROMPT.format(
            company_name=company_profile.name,
            industry=company_profile.industry,
            products_services=products_str,
            value_propositions=vp_str,
            icp_name=icp.icp_name,
            icp_description=icp.one_liner,
            demographics=demo_str,
            psychographics=psycho_str,
            motivations=motivations_str,
            pain_points=pains_str
        )
        
        # Call the LLM
        response = self.llm_client.analyze(
            prompt=prompt,
            model=self.analysis_model,
            system_prompt=(
                "You are a Value Proposition Canvas expert. "
                "Return only valid JSON."
            )
        )
        
        # Parse response
        vpc_data = self._extract_json(response.content)
        
        # Convert to VPC object
        vpc = self._parse_vpc(vpc_data, icp)
        
        logger.info(
            f"VPC complete for {icp.icp_name}. "
            f"Fit score: {vpc.fit_score}"
        )
        
        return vpc
    
    def _extract_json(self, content: str) -> Dict[str, Any]:
        """Extract JSON from LLM response."""
        if "```json" in content:
            start = content.find("```json") + 7
            end = content.find("```", start)
            if end > start:
                content = content[start:end].strip()
        elif "```" in content:
            start = content.find("```") + 3
            end = content.find("```", start)
            if end > start:
                content = content[start:end].strip()
        
        try:
            return json.loads(content)
        except json.JSONDecodeError as e:
            logger.error(f"Failed to parse VPC JSON: {e}")
            return {}
    
    def _parse_vpc(
        self,
        data: Dict[str, Any],
        icp: ICP
    ) -> ValuePropositionCanvas:
        """Parse VPC data into structured object."""
        
        # Parse pain relievers
        pain_relievers = []
        for pr in data.get("pain_relievers", []):
            pain_relievers.append(
                PainReliever(
                    pain_addressed=pr.get("pain_addressed", ""),
                    feature_or_capability=pr.get(
                        "feature_or_capability", ""
                    ),
                    how_relieved=pr.get("how_relieved", ""),
                    relief_significance=pr.get("relief_significance", 5)
                )
            )
        
        # Parse gain creators
        gain_creators = []
        for gc in data.get("gain_creators", []):
            gain_creators.append(
                GainCreator(
                    gain_created=gc.get("gain_created", ""),
                    feature_or_capability=gc.get(
                        "feature_or_capability", ""
                    ),
                    how_created=gc.get("how_created", ""),
                    creation_significance=gc.get("creation_significance", 5)
                )
            )
        
        return ValuePropositionCanvas(
            icp_name=icp.icp_name,
            customer_jobs=data.get("customer_jobs", {}),
            customer_pains=data.get("customer_pains", []),
            customer_gains=data.get("customer_gains", []),
            products_services_fit=data.get("products_services_fit", []),
            pain_relievers=pain_relievers,
            gain_creators=gain_creators,
            value_proposition_statement=data.get(
                "value_proposition_statement", ""
            ),
            fit_score=data.get("fit_score", 0),
            unique_differentiators=data.get("unique_differentiators", []),
            gaps_weaknesses=data.get("gaps_weaknesses", []),
            messaging_recommendations=data.get(
                "messaging_recommendations", []
            )
        )