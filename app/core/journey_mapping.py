"""
Journey Mapping Module
======================
Creates comprehensive 5-stage customer journey maps with content
recommendations for each ICP.
"""

import json
import logging
from typing import Dict, Any, List, Optional

from app.models.research_models import (
    ClientInput,
    CompanyProfile,
    ICP,
    ValuePropositionCanvas,
    PainPointTaxonomy,
    CustomerJourneyMap,
    JourneyStage,
    ContentIdea
)
from app.llm.openrouter_client import OpenRouterClient


logger = logging.getLogger(__name__)


JOURNEY_MAPPING_PROMPT = """
You are an expert customer journey strategist specializing in content
marketing and campaign planning. Your task is to create a comprehensive
5-stage customer journey map for a specific ICP.

## Company Context

**Company:** {company_name}
**Industry:** {industry}

**Products/Services:**
{products_services}

**Value Proposition:**
{value_proposition}

## ICP Profile

**ICP Name:** {icp_name}
**Description:** {icp_description}

**Key Characteristics:**
{icp_characteristics}

## Pain Point Summary

**Top Functional Pains:**
{functional_pains}

**Top Emotional Pains:**
{emotional_pains}

**Forces of Progress:**
{forces_summary}

## Your Task

Create a detailed 5-stage customer journey map with actionable content
and campaign recommendations for each stage.

### STAGE 1: AWARENESS
*Moving from "Unaware" to "Problem Aware"*

The customer experiences symptoms but hasn't diagnosed the problem.
They don't know solutions exist.

**Content Goal:** Help them recognize and name their problem.
**Psychology:** Validation, education, "So that's why..."

### STAGE 2: CONSIDERATION  
*Moving from "Problem Aware" to "Solution Aware"*

The customer knows they have a problem and starts exploring solution
categories (not specific vendors yet).

**Content Goal:** Educate on solution approaches and criteria.
**Psychology:** Evaluation, comparison of approaches, "What options exist?"

### STAGE 3: DECISION
*Moving from "Solution Aware" to "Product Aware" to "Purchase"*

The customer knows the solution category and is comparing specific
vendors/products. They're building a business case.

**Content Goal:** Prove you're the best choice, reduce risk.
**Psychology:** Validation, risk mitigation, "Why you vs. alternatives?"

### STAGE 4: ONBOARDING
*Post-Purchase: Achieving First Value*

The customer has bought and needs to see return on investment quickly.
High risk of churn if value isn't realized.

**Content Goal:** Accelerate time-to-value, build habits.
**Psychology:** Confidence, quick wins, "This was the right choice"

### STAGE 5: EXPANSION
*Retention, Upsell, and Advocacy*

The customer is getting value and can become a growth engine through
upsells, cross-sells, and referrals.

**Content Goal:** Deepen engagement, identify expansion opportunities.
**Psychology:** Mastery, status, "I'm an expert now"

## Output Format

For each stage, provide:

```json
{{
    "overall_timeline": "Typical total journey duration",
    "awareness_stage": {{
        "objective": "Primary goal for this stage",
        "customer_state": {{
            "knowledge_level": "What they know/don't know",
            "emotional_state": ["Feeling 1", "Feeling 2"],
            "key_questions": ["What they're asking themselves"]
        }},
        "content_themes": ["Theme 1", "Theme 2"],
        "content_ideas": [
            {{
                "title": "Content title",
                "format": "blog|video|quiz|infographic|webinar|etc",
                "hook": "What makes them click",
                "key_message": "Main takeaway",
                "cta": "Next step they should take"
            }}
        ],
        "preferred_channels": ["Channel 1", "Channel 2"],
        "targeting_criteria": ["Targeting parameter 1"],
        "kpis": ["KPI 1", "KPI 2"]
    }},
    "consideration_stage": {{
        "objective": "Primary goal",
        "customer_state": {{
            "knowledge_level": "What they know",
            "emotional_state": ["Feeling 1"],
            "key_questions": ["Question 1"]
        }},
        "content_themes": ["Theme 1"],
        "content_ideas": [
            {{
                "title": "Title",
                "format": "format",
                "hook": "Hook",
                "key_message": "Message",
                "cta": "CTA"
            }}
        ],
        "preferred_channels": ["Channel 1"],
        "comparison_criteria": ["What they compare on"],
        "kpis": ["KPI 1"]
    }},
    "decision_stage": {{
        "objective": "Primary goal",
        "customer_state": {{
            "knowledge_level": "What they know",
            "emotional_state": ["Feeling 1"],
            "key_questions": ["Question 1"]
        }},
        "content_themes": ["Theme 1"],
        "content_ideas": [
            {{
                "title": "Title",
                "format": "format",
                "hook": "Hook",
                "key_message": "Message",
                "cta": "CTA"
            }}
        ],
        "preferred_channels": ["Channel 1"],
        "objection_handlers": ["Objection 1: How to address"],
        "social_proof_needed": ["Type of proof 1"],
        "kpis": ["KPI 1"]
    }},
    "onboarding_stage": {{
        "objective": "Primary goal",
        "customer_state": {{
            "knowledge_level": "What they know",
            "emotional_state": ["Feeling 1"],
            "key_questions": ["Question 1"]
        }},
        "first_value_milestone": "What 'success' looks like initially",
        "content_themes": ["Theme 1"],
        "content_ideas": [
            {{
                "title": "Title",
                "format": "format",
                "hook": "Hook",
                "key_message": "Message",
                "cta": "CTA"
            }}
        ],
        "preferred_channels": ["Channel 1"],
        "activation_metrics": ["Metric 1"],
        "churn_risk_signals": ["Signal 1"],
        "kpis": ["KPI 1"]
    }},
    "expansion_stage": {{
        "objective": "Primary goal",
        "customer_state": {{
            "knowledge_level": "What they know",
            "emotional_state": ["Feeling 1"],
            "key_questions": ["Question 1"]
        }},
        "content_themes": ["Theme 1"],
        "content_ideas": [
            {{
                "title": "Title",
                "format": "format",
                "hook": "Hook",
                "key_message": "Message",
                "cta": "CTA"
            }}
        ],
        "preferred_channels": ["Channel 1"],
        "upsell_triggers": ["Trigger 1"],
        "referral_program_hooks": ["Hook for referrals"],
        "advocacy_opportunities": ["How to turn them into advocates"],
        "kpis": ["KPI 1"]
    }},
    "cross_stage_recommendations": [
        "Overall recommendation 1",
        "Overall recommendation 2"
    ],
    "content_calendar_priorities": [
        {{
            "priority": 1,
            "stage": "awareness|consideration|decision|onboarding|expansion",
            "content_type": "Type",
            "rationale": "Why this first"
        }}
    ]
}}
```

Generate the comprehensive journey map now:
"""


class JourneyMappingModule:
    """
    Creates 5-stage customer journey maps for each ICP.
    """
    
    def __init__(
        self,
        llm_client: OpenRouterClient,
        analysis_model: str
    ):
        """
        Initialize the journey mapping module.
        
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
        icp: ICP,
        value_proposition: Optional[ValuePropositionCanvas] = None,
        pain_taxonomy: Optional[PainPointTaxonomy] = None
    ) -> CustomerJourneyMap:
        """
        Generate customer journey map for the given ICP.
        
        Args:
            client_input: Original client input
            company_profile: Parsed company profile
            icp: The ICP to analyze
            value_proposition: Optional VPC for this ICP
            pain_taxonomy: Optional pain taxonomy for this ICP
            
        Returns:
            CustomerJourneyMap object
        """
        logger.info(f"Creating journey map for ICP: {icp.icp_name}")
        
        # Format products/services
        products_list = []
        for ps in company_profile.products_services:
            products_list.append(f"- {ps.name}: {ps.description}")
        products_str = "\n".join(products_list) or "Not specified"
        
        # Format value proposition
        vp_str = "Not analyzed"
        if value_proposition:
            vp_str = value_proposition.value_proposition_statement or ""
            if value_proposition.unique_differentiators:
                vp_str += "\n\nUnique Differentiators:\n"
                for d in value_proposition.unique_differentiators:
                    vp_str += f"- {d}\n"
        
        # Format ICP characteristics
        characteristics = [
            f"- Decision Style: {icp.psychographics.decision_style.value}",
            f"- Risk Tolerance: {icp.psychographics.risk_tolerance.value}"
        ]
        if icp.demographics.job_titles:
            titles = ", ".join(icp.demographics.job_titles[:3])
            characteristics.append(f"- Roles: {titles}")
        if icp.behavioral.research_channels:
            channels = ", ".join(icp.behavioral.research_channels[:5])
            characteristics.append(f"- Research Channels: {channels}")
        if icp.behavioral.decision_timeline:
            characteristics.append(
                f"- Decision Timeline: {icp.behavioral.decision_timeline}"
            )
        char_str = "\n".join(characteristics)
        
        # Format pains
        func_pains = []
        emot_pains = []
        
        if pain_taxonomy:
            for p in pain_taxonomy.functional_pains[:5]:
                func_pains.append(
                    f"- {p.statement} (Severity: {p.severity}/10)"
                )
            for p in pain_taxonomy.emotional_pains[:5]:
                emot_pains.append(
                    f"- {p.statement} (Severity: {p.severity}/10)"
                )
        else:
            # Fall back to ICP-level pains
            for p in icp.pain_points[:5]:
                if p.category in ["functional", "inefficiency", "complexity"]:
                    func_pains.append(
                        f"- {p.statement} (Severity: {p.severity}/10)"
                    )
                else:
                    emot_pains.append(
                        f"- {p.statement} (Severity: {p.severity}/10)"
                    )
        
        func_str = "\n".join(func_pains) or "Not specified"
        emot_str = "\n".join(emot_pains) or "Not specified"
        
        # Format forces summary
        forces_str = "Not analyzed"
        if pain_taxonomy and pain_taxonomy.forces_analysis:
            fa = pain_taxonomy.forces_analysis
            forces_parts = []
            if fa.push_factors:
                forces_parts.append(f"Push: {', '.join(fa.push_factors[:2])}")
            if fa.pull_factors:
                forces_parts.append(f"Pull: {', '.join(fa.pull_factors[:2])}")
            if fa.habit_factors:
                forces_parts.append(
                    f"Habit (resistance): {', '.join(fa.habit_factors[:2])}"
                )
            if fa.anxiety_factors:
                forces_parts.append(
                    f"Anxiety: {', '.join(fa.anxiety_factors[:2])}"
                )
            forces_str = "\n".join(forces_parts)
        
        # Build the prompt
        prompt = JOURNEY_MAPPING_PROMPT.format(
            company_name=company_profile.name,
            industry=company_profile.industry,
            products_services=products_str,
            value_proposition=vp_str,
            icp_name=icp.icp_name,
            icp_description=icp.one_liner,
            icp_characteristics=char_str,
            functional_pains=func_str,
            emotional_pains=emot_str,
            forces_summary=forces_str
        )
        
        # Call the LLM
        response = self.llm_client.analyze(
            prompt=prompt,
            model=self.analysis_model,
            system_prompt=(
                "You are a customer journey and content strategy expert. "
                "Return only valid JSON."
            )
        )
        
        # Parse response
        journey_data = self._extract_json(response.content)
        
        # Convert to journey map object
        journey = self._parse_journey(journey_data, icp)
        
        logger.info(f"Journey map complete for {icp.icp_name}")
        
        return journey
    
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
            logger.error(f"Failed to parse journey JSON: {e}")
            return {}
    
    def _parse_journey(
        self,
        data: Dict[str, Any],
        icp: ICP
    ) -> CustomerJourneyMap:
        """Parse journey data into structured object."""
        
        def parse_stage(stage_data: Dict[str, Any]) -> JourneyStage:
            """Parse a single stage."""
            if not stage_data:
                return None
            
            # Parse content ideas
            content_ideas = []
            for idea in stage_data.get("content_ideas", []):
                content_ideas.append(
                    ContentIdea(
                        title=idea.get("title", ""),
                        format=idea.get("format", "blog"),
                        hook=idea.get("hook"),
                        key_message=idea.get("key_message"),
                        cta=idea.get("cta")
                    )
                )
            
            # Extract customer state
            state = stage_data.get("customer_state", {})
            
            return JourneyStage(
                objective=stage_data.get("objective", ""),
                knowledge_level=state.get("knowledge_level"),
                emotional_state=state.get("emotional_state", []),
                key_questions=state.get("key_questions", []),
                content_themes=stage_data.get("content_themes", []),
                content_ideas=content_ideas,
                preferred_channels=stage_data.get("preferred_channels", []),
                targeting_criteria=stage_data.get("targeting_criteria", []),
                kpis=stage_data.get("kpis", [])
            )
        
        return CustomerJourneyMap(
            icp_name=icp.icp_name,
            overall_timeline=data.get("overall_timeline"),
            awareness_stage=parse_stage(data.get("awareness_stage", {})),
            consideration_stage=parse_stage(
                data.get("consideration_stage", {})
            ),
            decision_stage=parse_stage(data.get("decision_stage", {})),
            onboarding_stage=parse_stage(data.get("onboarding_stage", {})),
            expansion_stage=parse_stage(data.get("expansion_stage", {})),
            cross_stage_recommendations=data.get(
                "cross_stage_recommendations", []
            ),
            content_calendar_priorities=data.get(
                "content_calendar_priorities", []
            )
        )