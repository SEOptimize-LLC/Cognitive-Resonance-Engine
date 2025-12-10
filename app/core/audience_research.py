"""
Audience Research Module
========================
Generates Ideal Customer Profiles (ICPs) based on company data
and market research using advanced psychographic analysis.
"""

import json
import logging
from typing import Dict, Any, List

from app.models.research_models import (
    ClientInput,
    CompanyProfile,
    ICP,
    Demographics,
    Psychographics,
    BehavioralProfile,
    Motivation,
    PainPoint,
    DecisionStyle,
    RiskTolerance
)
from app.llm.openrouter_client import OpenRouterClient


logger = logging.getLogger(__name__)


ICP_GENERATION_PROMPT = """
You are an expert market researcher and customer strategist specializing in
psychographic segmentation and buyer persona development.

## Company Context

**Company:** {company_name}
**Industry:** {industry}
**Business Model:** {business_model}

**Company Overview:**
{company_overview}

**Products/Services:**
{products_services}

**Stated Value Propositions:**
{value_propositions}

**Stated Target Audience:**
{stated_audience}

**Competitive Landscape:**
{competitors}

**Market Trends:**
{market_trends}

## Your Task

Generate {num_icps} distinct Ideal Customer Profiles (ICPs) for this company.
Each ICP should represent a meaningfully different customer segment with unique
characteristics, motivations, and pain points.

For each ICP, provide comprehensive analysis across these dimensions:

### 1. Demographics/Firmographics
- Company size (for B2B) or age/income range (for B2C)
- Job titles and roles (decision makers and influencers)
- Industry verticals most likely to buy
- Geographic focus
- Budget range for this solution

### 2. Psychographics (Critical)
- Decision-making style (analytical, intuitive, consensus-driven, etc.)
- Risk tolerance (risk-averse, moderate, risk-seeking)
- Core professional/personal values
- Career/life aspirations and goals
- Biggest fears related to this purchase
- Status and perception concerns
- Personality tendencies

### 3. Behavioral Profile
- How they typically research solutions
- Decision timeline (fast/slow, who's involved)
- Preferred communication channels
- Content consumption habits
- Current tools/solutions they use
- Purchase triggers and signals

### 4. Motivations (Generate 5-7 per ICP)
For each motivation:
- Statement of what drives them
- Category (functional, social, emotional)
- Intensity (1-10)

### 5. Pain Points (Generate 5-7 per ICP)
For each pain point:
- Statement of the pain
- Category (functional, financial, emotional)
- Severity (1-10)
- How they currently cope

### 6. Priority and Narrative
- Segment priority (high, medium, low)
- A one-liner describing this ICP
- A detailed narrative paragraph bringing this persona to life

## Output Format

Return your analysis as a JSON array:

```json
[
    {{
        "icp_name": "Descriptive Name for this ICP",
        "one_liner": "Brief tagline describing this persona",
        "segment_priority": "high|medium|low",
        "demographics": {{
            "company_size": "10-50 employees",
            "job_titles": ["Title 1", "Title 2"],
            "seniority_level": "Director+",
            "industry_verticals": ["Industry 1", "Industry 2"],
            "geographic_focus": "North America",
            "budget_range": "$10,000 - $50,000/year",
            "age_range": "35-50",
            "income_range": "$100k-$200k",
            "education_level": "Bachelor's+"
        }},
        "psychographics": {{
            "decision_style": "analytical|intuitive|consensus|delegator",
            "risk_tolerance": "risk_averse|moderate|risk_seeking",
            "core_values": ["Value 1", "Value 2", "Value 3"],
            "aspirations": ["Goal 1", "Goal 2"],
            "fears": ["Fear 1", "Fear 2"],
            "status_concerns": ["Concern 1"],
            "personality_traits": ["Trait 1", "Trait 2"]
        }},
        "behavioral": {{
            "research_channels": ["Channel 1", "Channel 2"],
            "decision_timeline": "2-4 weeks typical",
            "decision_influencers": ["Role 1", "Role 2"],
            "content_preferences": ["Webinars", "Case Studies"],
            "current_solutions": ["Tool A", "Manual Process"],
            "purchase_triggers": ["Trigger 1", "Trigger 2"],
            "objections": ["Objection 1", "Objection 2"]
        }},
        "motivations": [
            {{
                "statement": "Motivation statement",
                "category": "functional|social|emotional",
                "intensity": 8
            }}
        ],
        "pain_points": [
            {{
                "statement": "Pain point statement",
                "category": "functional|financial|emotional",
                "severity": 9,
                "current_coping": "How they currently deal with it"
            }}
        ],
        "detailed_narrative": "A 3-4 sentence paragraph bringing this persona to life with specific details, day-in-the-life elements, and emotional resonance."
    }}
]
```

## Guidelines

1. **Make ICPs Distinct**: Each ICP should be meaningfully different, not just
   slight variations. Think about different stages of business maturity,
   different use cases, different buyer motivations.

2. **Be Specific**: Avoid generic descriptions. Include specific job titles,
   company sizes, industries, and concrete behaviors.

3. **Prioritize Correctly**: High priority = largest revenue opportunity +
   best product fit. Not all ICPs should be "high."

4. **Psychographics are Key**: The emotional and psychological dimensions
   often determine purchase decisions more than demographics.

5. **Ground in Reality**: Base your ICPs on the company's actual offerings
   and market position, not hypothetical ideal scenarios.

Generate {num_icps} comprehensive ICPs now:
"""


class AudienceResearchModule:
    """
    Generates Ideal Customer Profiles from company research data.
    """
    
    def __init__(
        self,
        llm_client: OpenRouterClient,
        analysis_model: str
    ):
        """
        Initialize the audience research module.
        
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
        raw_research: Dict[str, Any],
        num_icps: int = 3
    ) -> List[ICP]:
        """
        Generate ICPs for the given company.
        
        Args:
            client_input: Original client input
            company_profile: Parsed company profile
            raw_research: Raw research data
            num_icps: Number of ICPs to generate
            
        Returns:
            List of ICP objects
        """
        logger.info(
            f"Generating {num_icps} ICPs for: {company_profile.name}"
        )
        
        # Format products/services
        products_list = []
        for ps in company_profile.products_services:
            products_list.append(
                f"- **{ps.name}**: {ps.description}"
            )
        products_str = "\n".join(products_list) if products_list else "Not specified"
        
        # Format value propositions
        vp_str = "\n".join(
            f"- {vp}" for vp in company_profile.stated_value_propositions
        ) if company_profile.stated_value_propositions else "Not specified"
        
        # Format competitors
        comp_list = []
        for comp in company_profile.competitors[:5]:  # Top 5
            comp_list.append(
                f"- **{comp.name}**: {comp.description or 'No description'}"
            )
        comp_str = "\n".join(comp_list) if comp_list else "Not specified"
        
        # Format market trends
        trends_str = "\n".join(
            f"- {trend}" for trend in company_profile.market_trends
        ) if company_profile.market_trends else "Not specified"
        
        # Build the prompt
        prompt = ICP_GENERATION_PROMPT.format(
            company_name=company_profile.name,
            industry=company_profile.industry,
            business_model=company_profile.business_model.value,
            company_overview=company_profile.overview,
            products_services=products_str,
            value_propositions=vp_str,
            stated_audience=company_profile.stated_target_audience or "Not specified",
            competitors=comp_str,
            market_trends=trends_str,
            num_icps=num_icps
        )
        
        # Call the LLM
        response = self.llm_client.analyze(
            prompt=prompt,
            model=self.analysis_model,
            system_prompt=(
                "You are an expert market researcher specializing in "
                "psychographic segmentation. Return only valid JSON."
            )
        )
        
        # Parse response
        icp_data = self._extract_json(response.content)
        
        # Convert to ICP objects
        icps = []
        for data in icp_data:
            icp = self._parse_icp(data)
            icps.append(icp)
        
        logger.info(f"Generated {len(icps)} ICPs")
        return icps
    
    def _extract_json(self, content: str) -> List[Dict[str, Any]]:
        """Extract JSON array from LLM response."""
        # Try to find JSON in code blocks
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
        
        # Find array bounds
        start_bracket = content.find("[")
        end_bracket = content.rfind("]")
        if start_bracket >= 0 and end_bracket > start_bracket:
            content = content[start_bracket:end_bracket + 1]
        
        try:
            data = json.loads(content)
            if isinstance(data, list):
                return data
            return [data]
        except json.JSONDecodeError as e:
            logger.error(f"Failed to parse ICP JSON: {e}")
            return []
    
    def _parse_icp(self, data: Dict[str, Any]) -> ICP:
        """Parse a single ICP from JSON data."""
        
        # Parse demographics
        demo_data = data.get("demographics", {})
        demographics = Demographics(
            company_size=demo_data.get("company_size"),
            job_titles=demo_data.get("job_titles", []),
            seniority_level=demo_data.get("seniority_level"),
            industry_verticals=demo_data.get("industry_verticals", []),
            geographic_focus=demo_data.get("geographic_focus"),
            budget_range=demo_data.get("budget_range"),
            age_range=demo_data.get("age_range"),
            income_range=demo_data.get("income_range"),
            education_level=demo_data.get("education_level")
        )
        
        # Parse psychographics
        psycho_data = data.get("psychographics", {})
        
        # Map decision style
        decision_style_map = {
            "analytical": DecisionStyle.ANALYTICAL,
            "intuitive": DecisionStyle.INTUITIVE,
            "consensus": DecisionStyle.CONSENSUS,
            "delegator": DecisionStyle.DELEGATOR
        }
        decision_style = decision_style_map.get(
            psycho_data.get("decision_style", "").lower(),
            DecisionStyle.ANALYTICAL
        )
        
        # Map risk tolerance
        risk_map = {
            "risk_averse": RiskTolerance.RISK_AVERSE,
            "risk-averse": RiskTolerance.RISK_AVERSE,
            "moderate": RiskTolerance.MODERATE,
            "risk_seeking": RiskTolerance.RISK_SEEKING,
            "risk-seeking": RiskTolerance.RISK_SEEKING
        }
        risk_tolerance = risk_map.get(
            psycho_data.get("risk_tolerance", "").lower(),
            RiskTolerance.MODERATE
        )
        
        psychographics = Psychographics(
            decision_style=decision_style,
            risk_tolerance=risk_tolerance,
            core_values=psycho_data.get("core_values", []),
            aspirations=psycho_data.get("aspirations", []),
            fears=psycho_data.get("fears", []),
            status_concerns=psycho_data.get("status_concerns", []),
            personality_traits=psycho_data.get("personality_traits", [])
        )
        
        # Parse behavioral
        behav_data = data.get("behavioral", {})
        behavioral = BehavioralProfile(
            research_channels=behav_data.get("research_channels", []),
            decision_timeline=behav_data.get("decision_timeline"),
            decision_influencers=behav_data.get("decision_influencers", []),
            content_preferences=behav_data.get("content_preferences", []),
            current_solutions=behav_data.get("current_solutions", []),
            purchase_triggers=behav_data.get("purchase_triggers", []),
            objections=behav_data.get("objections", [])
        )
        
        # Parse motivations
        motivations = []
        for m in data.get("motivations", []):
            motivations.append(
                Motivation(
                    statement=m.get("statement", ""),
                    category=m.get("category", "functional"),
                    intensity=m.get("intensity", 5)
                )
            )
        
        # Parse pain points
        pain_points = []
        for p in data.get("pain_points", []):
            pain_points.append(
                PainPoint(
                    statement=p.get("statement", ""),
                    category=p.get("category", "functional"),
                    severity=p.get("severity", 5),
                    current_coping=p.get("current_coping")
                )
            )
        
        return ICP(
            icp_name=data.get("icp_name", "Unnamed ICP"),
            one_liner=data.get("one_liner", ""),
            segment_priority=data.get("segment_priority", "medium"),
            demographics=demographics,
            psychographics=psychographics,
            behavioral=behavioral,
            motivations=motivations,
            pain_points=pain_points,
            detailed_narrative=data.get("detailed_narrative", "")
        )