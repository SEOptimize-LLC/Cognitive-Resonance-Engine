"""
Data Ingestion Module
=====================
Uses Perplexity Sonar Deep Research to gather comprehensive information
about a client from their website and other sources.
"""

import json
import logging
from typing import Dict, Any, Tuple, Optional

from app.models.research_models import (
    ClientInput,
    CompanyProfile,
    ProductService,
    Competitor,
    BusinessModelType
)
from app.llm.openrouter_client import OpenRouterClient


logger = logging.getLogger(__name__)


# Prompt templates for data ingestion
COMPANY_RESEARCH_PROMPT = """
You are a business intelligence researcher conducting a comprehensive analysis
of a company for marketing strategy purposes.

Research the following company thoroughly:

**Company Name:** {client_name}
**Website:** {website_url}
**Industry:** {industry}
**Business Model:** {business_model}

{additional_urls_section}

{additional_context_section}

## Research Objectives

Please gather the following information:

### 1. Company Overview
- Company history and founding story
- Mission and vision statements
- Core values and culture
- Company size and structure (if available)
- Geographic presence and markets served

### 2. Products and Services
For each major product/service:
- Name and description
- Key features and capabilities
- Target audience for this specific offering
- Pricing model (if publicly available)
- Unique selling points

### 3. Value Propositions
- Stated value propositions from their website
- Key benefits they emphasize
- Transformation they promise customers
- Guarantees or risk-reversals offered

### 4. Target Audience (as stated by the company)
- Who they say they serve
- Customer segments they mention
- Use cases they highlight
- Customer testimonials/case studies themes

### 5. Brand Voice and Messaging
- Tone of their content (formal, casual, technical, etc.)
- Key themes and messaging patterns
- Language and terminology used
- Emotional appeals in their copy

### 6. Competitive Positioning
- How they differentiate themselves
- Competitors they mention or compare to
- Market positioning statements

### 7. Content and Thought Leadership
- Blog topics and themes
- Resources they offer (guides, tools, templates)
- Industries they write about
- Problems they address in content

Provide a comprehensive, structured analysis based on the information 
available on their website and public sources.

**IMPORTANT:** Return your findings in the following JSON format:

```json
{{
    "name": "Company Name",
    "overview": "Comprehensive company overview paragraph",
    "industry": "{industry}",
    "business_model": "{business_model}",
    "founding_story": "Brief founding story if available",
    "mission_statement": "Mission statement if available",
    "vision_statement": "Vision statement if available",
    "core_values": ["value1", "value2"],
    "company_size": "Size description if available",
    "geographic_presence": "Markets served",
    "products_services": [
        {{
            "name": "Product/Service Name",
            "description": "Description",
            "features": ["feature1", "feature2"],
            "target_audience": "Who it's for",
            "unique_aspects": ["unique1", "unique2"]
        }}
    ],
    "stated_value_propositions": [
        "Value prop 1",
        "Value prop 2"
    ],
    "stated_target_audience": "Who they say they serve",
    "brand_voice": {{
        "tone": "formal/casual/technical/friendly/etc",
        "key_themes": ["theme1", "theme2"],
        "emotional_appeals": ["appeal1", "appeal2"]
    }},
    "competitors": [
        {{
            "name": "Competitor Name",
            "description": "Brief description",
            "key_differentiators": ["diff1", "diff2"]
        }}
    ],
    "content_themes": ["theme1", "theme2"],
    "customer_testimonial_themes": ["theme1", "theme2"],
    "pricing_model": "Pricing approach if public",
    "guarantees": ["guarantee1"],
    "additional_insights": "Any other relevant insights"
}}
```
"""

COMPETITOR_RESEARCH_PROMPT = """
Research the competitive landscape for this company:

**Company:** {client_name}
**Industry:** {industry}
**Website:** {website_url}

{known_competitors_section}

## Research Objectives

1. **Identify Key Competitors**
   - Direct competitors (same product/service)
   - Indirect competitors (different solution, same problem)
   - Market leaders in this space

2. **Competitive Analysis**
   For each competitor:
   - Company name and website
   - Brief description of offerings
   - Key strengths and differentiators
   - Target audience
   - Pricing approach (if public)
   - Market positioning

3. **Market Gaps and Opportunities**
   - Underserved segments
   - Common complaints about existing solutions
   - Market trends and emerging needs

Return your findings in JSON format:

```json
{{
    "direct_competitors": [
        {{
            "name": "Competitor Name",
            "website": "URL",
            "description": "Description",
            "key_strengths": ["strength1", "strength2"],
            "key_differentiators": ["diff1", "diff2"],
            "target_audience": "Who they serve",
            "pricing_approach": "Pricing model",
            "market_position": "Leader/Challenger/Niche"
        }}
    ],
    "indirect_competitors": [
        {{
            "name": "Name",
            "description": "Description",
            "alternative_solution": "What they offer instead"
        }}
    ],
    "market_gaps": [
        "Gap 1",
        "Gap 2"
    ],
    "market_trends": [
        "Trend 1",
        "Trend 2"
    ],
    "common_complaints": [
        "Complaint about existing solutions"
    ]
}}
```
"""


class DataIngestionModule:
    """
    Handles data gathering about the client company using Perplexity Sonar.
    """
    
    def __init__(
        self,
        llm_client: OpenRouterClient,
        research_model: str
    ):
        """
        Initialize the data ingestion module.
        
        Args:
            llm_client: The OpenRouter client for API calls
            research_model: The model ID for research (Perplexity Sonar)
        """
        self.llm_client = llm_client
        self.research_model = research_model
    
    def run(
        self,
        client_input: ClientInput
    ) -> Tuple[CompanyProfile, Dict[str, Any]]:
        """
        Execute data ingestion for the given client.
        
        Args:
            client_input: The client information to research
            
        Returns:
            Tuple of (CompanyProfile, raw_research_data)
        """
        logger.info(f"Starting data ingestion for: {client_input.client_name}")
        
        # Gather raw research data
        raw_data = {}
        
        # Primary company research
        company_data = self._research_company(client_input)
        raw_data["company_research"] = company_data
        
        # Competitor research
        competitor_data = self._research_competitors(client_input)
        raw_data["competitor_research"] = competitor_data
        
        # Parse into structured profile
        company_profile = self._parse_company_profile(
            company_data,
            competitor_data,
            client_input
        )
        
        logger.info(f"Data ingestion complete for: {company_profile.name}")
        
        return company_profile, raw_data
    
    def _research_company(
        self,
        client_input: ClientInput
    ) -> Dict[str, Any]:
        """
        Research the company using Perplexity Sonar.
        """
        # Build URL section
        additional_urls = ""
        if client_input.about_page_url:
            additional_urls += f"\n**About Page:** {client_input.about_page_url}"
        if client_input.products_services_url:
            additional_urls += (
                f"\n**Products/Services Page:** "
                f"{client_input.products_services_url}"
            )
        if client_input.additional_urls:
            for url in client_input.additional_urls:
                additional_urls += f"\n**Additional URL:** {url}"
        
        additional_urls_section = ""
        if additional_urls:
            additional_urls_section = (
                f"**Additional Pages to Research:**{additional_urls}"
            )
        
        # Build context section
        additional_context_section = ""
        if client_input.additional_context:
            additional_context_section = (
                f"**Additional Context:**\n{client_input.additional_context}"
            )
        
        # Format the prompt
        prompt = COMPANY_RESEARCH_PROMPT.format(
            client_name=client_input.client_name,
            website_url=client_input.website_url,
            industry=client_input.industry,
            business_model=client_input.business_model.value,
            additional_urls_section=additional_urls_section,
            additional_context_section=additional_context_section
        )
        
        # Call Perplexity Sonar
        response = self.llm_client.research(
            query=prompt,
            model=self.research_model
        )
        
        # Parse JSON from response
        return self._extract_json(response.content)
    
    def _research_competitors(
        self,
        client_input: ClientInput
    ) -> Dict[str, Any]:
        """
        Research competitors using Perplexity Sonar.
        """
        known_competitors_section = ""
        if client_input.known_competitors:
            known_competitors_section = (
                f"**Known Competitors (verify and expand):**\n"
                f"{client_input.known_competitors}"
            )
        
        prompt = COMPETITOR_RESEARCH_PROMPT.format(
            client_name=client_input.client_name,
            industry=client_input.industry,
            website_url=client_input.website_url,
            known_competitors_section=known_competitors_section
        )
        
        response = self.llm_client.research(
            query=prompt,
            model=self.research_model
        )
        
        return self._extract_json(response.content)
    
    def _extract_json(self, content: str) -> Dict[str, Any]:
        """
        Extract JSON from LLM response content.
        
        Handles cases where JSON is wrapped in markdown code blocks.
        """
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
        
        try:
            return json.loads(content)
        except json.JSONDecodeError as e:
            logger.warning(f"Failed to parse JSON: {e}")
            # Return raw content wrapped in a dict
            return {"raw_content": content, "parse_error": str(e)}
    
    def _parse_company_profile(
        self,
        company_data: Dict[str, Any],
        competitor_data: Dict[str, Any],
        client_input: ClientInput
    ) -> CompanyProfile:
        """
        Parse raw research data into a structured CompanyProfile.
        """
        # Handle parse errors
        if "parse_error" in company_data:
            logger.warning(
                "Using fallback parsing due to JSON error"
            )
            return self._fallback_parse(client_input)
        
        # Parse products/services
        products_services = []
        for ps in company_data.get("products_services", []):
            products_services.append(
                ProductService(
                    name=ps.get("name", "Unknown"),
                    description=ps.get("description", ""),
                    features=ps.get("features", []),
                    target_audience=ps.get("target_audience"),
                    unique_aspects=ps.get("unique_aspects", [])
                )
            )
        
        # Parse competitors
        competitors = []
        
        # From company research
        for comp in company_data.get("competitors", []):
            competitors.append(
                Competitor(
                    name=comp.get("name", "Unknown"),
                    description=comp.get("description"),
                    key_differentiators=comp.get("key_differentiators", [])
                )
            )
        
        # From competitor research
        for comp in competitor_data.get("direct_competitors", []):
            # Avoid duplicates
            if not any(c.name == comp.get("name") for c in competitors):
                competitors.append(
                    Competitor(
                        name=comp.get("name", "Unknown"),
                        website=comp.get("website"),
                        description=comp.get("description"),
                        key_differentiators=comp.get(
                            "key_differentiators", []
                        ),
                        target_audience=comp.get("target_audience"),
                        market_position=comp.get("market_position")
                    )
                )
        
        # Parse business model
        bm_str = company_data.get("business_model", "").lower()
        if "b2b" in bm_str and "b2c" in bm_str:
            business_model = BusinessModelType.BOTH
        elif "b2c" in bm_str:
            business_model = BusinessModelType.B2C
        else:
            business_model = BusinessModelType.B2B
        
        # Build the profile
        return CompanyProfile(
            name=company_data.get("name", client_input.client_name),
            website_url=client_input.website_url,
            overview=company_data.get("overview", ""),
            industry=company_data.get("industry", client_input.industry),
            business_model=business_model,
            founding_story=company_data.get("founding_story"),
            mission_statement=company_data.get("mission_statement"),
            vision_statement=company_data.get("vision_statement"),
            core_values=company_data.get("core_values", []),
            products_services=products_services,
            stated_value_propositions=company_data.get(
                "stated_value_propositions", []
            ),
            stated_target_audience=company_data.get("stated_target_audience"),
            brand_voice=company_data.get("brand_voice", {}),
            competitors=competitors,
            content_themes=company_data.get("content_themes", []),
            market_gaps=competitor_data.get("market_gaps", []),
            market_trends=competitor_data.get("market_trends", [])
        )
    
    def _fallback_parse(
        self,
        client_input: ClientInput
    ) -> CompanyProfile:
        """
        Create a minimal profile when parsing fails.
        """
        return CompanyProfile(
            name=client_input.client_name,
            website_url=client_input.website_url,
            overview=(
                f"{client_input.client_name} is a company in the "
                f"{client_input.industry} industry."
            ),
            industry=client_input.industry,
            business_model=client_input.business_model,
            products_services=[],
            stated_value_propositions=[],
            competitors=[]
        )