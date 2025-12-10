"""
Pain Taxonomy Module
====================
Creates comprehensive pain point analysis using the Jobs-to-be-Done (JTBD)
framework and the Four Forces of Progress model.
"""

import json
import logging
from typing import Dict, Any, List, Optional

from app.models.research_models import (
    ClientInput,
    CompanyProfile,
    ICP,
    PainPointTaxonomy,
    DetailedPainPoint,
    ForcesOfProgressAnalysis
)
from app.llm.openrouter_client import OpenRouterClient


logger = logging.getLogger(__name__)


PAIN_TAXONOMY_PROMPT = """
You are an expert in Jobs-to-be-Done (JTBD) theory and customer psychology.
Your task is to create a comprehensive pain point taxonomy for a specific
customer segment.

## Company Context

**Company:** {company_name}
**Industry:** {industry}
**Solution Category:** {solution_category}

**Company Value Proposition:**
{value_proposition}

## Target ICP Profile

**ICP Name:** {icp_name}
**One-Liner:** {icp_one_liner}

**Key Characteristics:**
{icp_characteristics}

**Known Pain Points:**
{known_pain_points}

**Known Motivations:**
{known_motivations}

## Your Task

Create an exhaustive pain point taxonomy organized into three dimensions,
plus a Forces of Progress analysis.

### 1. FUNCTIONAL PAIN POINTS
Pains related to getting the job done effectively.

Categories:
- **Inefficiency**: Time waste, slow processes, manual work
- **Complexity**: Hard to learn, hard to use, confusing
- **Inaccuracy**: Errors, inconsistencies, unreliable results
- **Lack of Capability**: Missing features, limitations
- **Interoperability**: Integration issues, data silos
- **Scalability**: Can't grow, breaks under load
- **Reliability**: Downtime, crashes, data loss

### 2. FINANCIAL PAIN POINTS
Pains related to cost and resources.

Categories:
- **Direct Cost**: Subscription, licenses, fees
- **Hidden Costs**: Maintenance, training, customization
- **Opportunity Cost**: What else could this budget do?
- **ROI Uncertainty**: Can't prove value, unclear payback
- **Cash Flow**: Upfront costs, payment terms
- **Resource Drain**: Staff time, IT overhead

### 3. EMOTIONAL/PSYCHOLOGICAL PAIN POINTS
Internal friction and fears.

Categories:
- **Anxiety**: Fear of failure, making wrong choice
- **Frustration**: Repeated disappointments, unmet promises
- **Overwhelm**: Too many options, analysis paralysis
- **Imposter Syndrome**: Not feeling capable/qualified
- **Status Risk**: Looking bad to peers/superiors
- **Trust Issues**: Burned by vendors before
- **Change Fatigue**: Tired of switching solutions

### 4. FORCES OF PROGRESS ANALYSIS
The JTBD Four Forces model:

- **Push** (away from current situation): What's pushing them to change?
- **Pull** (toward new solution): What's attracting them to a new solution?
- **Habit** (resistance to change): What keeps them using current approach?
- **Anxiety** (fear of new): What makes them nervous about switching?

Analyze the balance of forces and recommend where to focus.

## Output Format

```json
{{
    "functional_pains": [
        {{
            "statement": "Clear description of the pain",
            "category": "inefficiency|complexity|inaccuracy|capability|interoperability|scalability|reliability",
            "severity": 8,
            "frequency": "daily|weekly|monthly|quarterly",
            "current_coping_mechanism": "How they currently deal with it",
            "impact_if_unresolved": "Business consequence of not solving",
            "root_cause": "Underlying cause of this pain",
            "five_whys_depth": "The deepest 'why' behind this pain"
        }}
    ],
    "financial_pains": [
        {{
            "statement": "Clear description of the financial pain",
            "category": "direct_cost|hidden_cost|opportunity_cost|roi_uncertainty|cash_flow|resource_drain",
            "severity": 7,
            "frequency": "monthly",
            "estimated_cost_impact": "$X per month/year",
            "current_coping_mechanism": "How they manage this cost",
            "impact_if_unresolved": "Financial consequence",
            "root_cause": "Why this cost exists"
        }}
    ],
    "emotional_pains": [
        {{
            "statement": "Clear description of the emotional pain",
            "category": "anxiety|frustration|overwhelm|imposter_syndrome|status_risk|trust_issues|change_fatigue",
            "severity": 9,
            "frequency": "situational",
            "trigger_situations": ["When this feeling arises"],
            "current_coping_mechanism": "How they manage emotionally",
            "impact_if_unresolved": "Personal/professional consequence",
            "underlying_fear": "The core fear or need behind this"
        }}
    ],
    "forces_analysis": {{
        "push_factors": [
            {{
                "factor": "Description of push factor",
                "strength": 8,
                "triggering_events": ["Event that activates this"]
            }}
        ],
        "pull_factors": [
            {{
                "factor": "Description of pull factor",
                "strength": 7,
                "desired_outcomes": ["What they hope to achieve"]
            }}
        ],
        "habit_factors": [
            {{
                "factor": "Description of inertia/habit",
                "strength": 6,
                "switching_cost": "What it takes to overcome"
            }}
        ],
        "anxiety_factors": [
            {{
                "factor": "Description of anxiety about change",
                "strength": 7,
                "mitigation_needed": "What would reduce this anxiety"
            }}
        ],
        "net_force_assessment": "Overall assessment of whether forces favor change",
        "recommended_focus": "Where marketing should focus to tip the balance",
        "key_trigger_moments": ["Moments when they're most likely to switch"]
    }},
    "pain_priority_ranking": [
        {{
            "pain": "Description",
            "dimension": "functional|financial|emotional",
            "priority_score": 95,
            "rationale": "Why this should be addressed first"
        }}
    ],
    "messaging_implications": [
        "Lead with X because this ICP cares most about...",
        "Avoid Y messaging because..."
    ]
}}
```

Generate the comprehensive pain taxonomy now:
"""


class PainTaxonomyModule:
    """
    Creates comprehensive pain point taxonomy for each ICP.
    """
    
    def __init__(
        self,
        llm_client: OpenRouterClient,
        analysis_model: str
    ):
        """
        Initialize the pain taxonomy module.
        
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
    ) -> PainPointTaxonomy:
        """
        Generate pain taxonomy for the given ICP.
        
        Args:
            client_input: Original client input
            company_profile: Parsed company profile
            icp: The ICP to analyze
            
        Returns:
            PainPointTaxonomy object
        """
        logger.info(f"Creating pain taxonomy for ICP: {icp.icp_name}")
        
        # Format solution category
        products = [ps.name for ps in company_profile.products_services]
        solution_category = ", ".join(products) or company_profile.industry
        
        # Format value proposition
        vp_list = company_profile.stated_value_propositions or []
        vp_str = "\n".join(f"- {vp}" for vp in vp_list) or "Not specified"
        
        # Format ICP characteristics
        characteristics = [
            f"- Decision Style: {icp.psychographics.decision_style.value}",
            f"- Risk Tolerance: {icp.psychographics.risk_tolerance.value}"
        ]
        if icp.demographics.job_titles:
            titles = ", ".join(icp.demographics.job_titles[:3])
            characteristics.append(f"- Job Titles: {titles}")
        if icp.demographics.company_size:
            characteristics.append(
                f"- Company Size: {icp.demographics.company_size}"
            )
        if icp.psychographics.fears:
            fears = ", ".join(icp.psychographics.fears[:3])
            characteristics.append(f"- Key Fears: {fears}")
        char_str = "\n".join(characteristics)
        
        # Format known pain points
        pains_list = [
            f"- {p.statement} ({p.category}, Severity: {p.severity}/10)"
            for p in icp.pain_points
        ]
        pains_str = "\n".join(pains_list) or "None previously identified"
        
        # Format known motivations
        motivations_list = [
            f"- {m.statement} ({m.category}, Intensity: {m.intensity}/10)"
            for m in icp.motivations
        ]
        motivations_str = "\n".join(motivations_list) or "None specified"
        
        # Build the prompt
        prompt = PAIN_TAXONOMY_PROMPT.format(
            company_name=company_profile.name,
            industry=company_profile.industry,
            solution_category=solution_category,
            value_proposition=vp_str,
            icp_name=icp.icp_name,
            icp_one_liner=icp.one_liner,
            icp_characteristics=char_str,
            known_pain_points=pains_str,
            known_motivations=motivations_str
        )
        
        # Call the LLM
        response = self.llm_client.analyze(
            prompt=prompt,
            model=self.analysis_model,
            system_prompt=(
                "You are a JTBD and customer psychology expert. "
                "Return only valid JSON."
            )
        )
        
        # Parse response
        taxonomy_data = self._extract_json(response.content)
        
        # Convert to taxonomy object
        taxonomy = self._parse_taxonomy(taxonomy_data, icp)
        
        total_pains = (
            len(taxonomy.functional_pains) +
            len(taxonomy.financial_pains) +
            len(taxonomy.emotional_pains)
        )
        
        logger.info(
            f"Pain taxonomy complete for {icp.icp_name}. "
            f"Total pains: {total_pains}"
        )
        
        return taxonomy
    
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
            logger.error(f"Failed to parse taxonomy JSON: {e}")
            return {}
    
    def _parse_taxonomy(
        self,
        data: Dict[str, Any],
        icp: ICP
    ) -> PainPointTaxonomy:
        """Parse taxonomy data into structured object."""
        
        # Parse functional pains
        functional_pains = []
        for p in data.get("functional_pains", []):
            functional_pains.append(
                DetailedPainPoint(
                    statement=p.get("statement", ""),
                    category=p.get("category", "inefficiency"),
                    severity=p.get("severity", 5),
                    frequency=p.get("frequency"),
                    current_coping_mechanism=p.get("current_coping_mechanism"),
                    impact_if_unresolved=p.get("impact_if_unresolved"),
                    root_cause=p.get("root_cause"),
                    five_whys_depth=p.get("five_whys_depth")
                )
            )
        
        # Parse financial pains
        financial_pains = []
        for p in data.get("financial_pains", []):
            financial_pains.append(
                DetailedPainPoint(
                    statement=p.get("statement", ""),
                    category=p.get("category", "direct_cost"),
                    severity=p.get("severity", 5),
                    frequency=p.get("frequency"),
                    current_coping_mechanism=p.get("current_coping_mechanism"),
                    impact_if_unresolved=p.get("impact_if_unresolved"),
                    root_cause=p.get("root_cause"),
                    estimated_cost_impact=p.get("estimated_cost_impact")
                )
            )
        
        # Parse emotional pains
        emotional_pains = []
        for p in data.get("emotional_pains", []):
            emotional_pains.append(
                DetailedPainPoint(
                    statement=p.get("statement", ""),
                    category=p.get("category", "anxiety"),
                    severity=p.get("severity", 5),
                    frequency=p.get("frequency"),
                    current_coping_mechanism=p.get("current_coping_mechanism"),
                    impact_if_unresolved=p.get("impact_if_unresolved"),
                    trigger_situations=p.get("trigger_situations", []),
                    underlying_fear=p.get("underlying_fear")
                )
            )
        
        # Parse forces analysis
        forces_data = data.get("forces_analysis", {})
        forces_analysis = None
        
        if forces_data:
            forces_analysis = ForcesOfProgressAnalysis(
                push_factors=[
                    f.get("factor", "") for f in forces_data.get(
                        "push_factors", []
                    )
                ],
                pull_factors=[
                    f.get("factor", "") for f in forces_data.get(
                        "pull_factors", []
                    )
                ],
                habit_factors=[
                    f.get("factor", "") for f in forces_data.get(
                        "habit_factors", []
                    )
                ],
                anxiety_factors=[
                    f.get("factor", "") for f in forces_data.get(
                        "anxiety_factors", []
                    )
                ],
                net_force_assessment=forces_data.get("net_force_assessment"),
                recommended_focus=forces_data.get("recommended_focus"),
                key_trigger_moments=forces_data.get("key_trigger_moments", [])
            )
        
        return PainPointTaxonomy(
            icp_name=icp.icp_name,
            functional_pains=functional_pains,
            financial_pains=financial_pains,
            emotional_pains=emotional_pains,
            forces_analysis=forces_analysis,
            pain_priority_ranking=data.get("pain_priority_ranking", []),
            messaging_implications=data.get("messaging_implications", [])
        )