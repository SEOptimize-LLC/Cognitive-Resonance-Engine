# Data Ingestion Prompts

## Prompt 1: Company Overview Research

```
You are an expert business analyst conducting comprehensive research on a company. Your goal is to gather and synthesize all available public information about the business.

COMPANY INFORMATION:
- Company Name: {company_name}
- Website URL: {website_url}
- About Page: {about_url}
- Products/Services Page: {products_url}
- Additional URLs: {additional_urls}
- Industry: {industry}
- Business Model: {business_model}
- Additional Context: {additional_context}

Conduct thorough research and provide a comprehensive analysis covering:

## 1. COMPANY OVERVIEW
- Full legal name and any DBA names
- Year founded and brief history
- Headquarters location
- Company size (employees, if available)
- Funding status (if startup/private)
- Key leadership (CEO, founders)
- Mission statement
- Vision statement

## 2. BUSINESS MODEL ANALYSIS
- Primary revenue model
- B2B vs B2C vs Both
- Target market segments
- Geographic focus
- Pricing strategy indicators

## 3. PRODUCTS & SERVICES INVENTORY
For each product/service identified:
- Name
- Description
- Key features (bullet points)
- Target user/buyer
- Pricing tier (if visible)
- Unique aspects

## 4. VALUE PROPOSITIONS (As Stated by Company)
List all value propositions you can identify from their messaging:
- Primary value proposition
- Secondary value propositions
- Proof points or evidence they cite
- Guarantees or promises made

## 5. BRAND VOICE & MESSAGING ANALYSIS
- Tone (formal/casual/technical/friendly)
- Language complexity level
- Key messaging themes
- Recurring phrases or taglines
- Emotional appeals used

## 6. TARGET AUDIENCE INDICATORS
Based on their messaging, identify:
- Who they seem to be targeting
- Industries mentioned
- Job titles or roles referenced
- Company sizes targeted
- Pain points they address in their copy

## 7. COMPETITIVE POSITIONING
- How they position against competitors
- Mentioned competitors (if any)
- Claimed differentiators
- Market category they claim

## 8. TRUST SIGNALS
- Customer testimonials
- Case studies mentioned
- Awards or recognition
- Certifications
- Media mentions
- Partnership logos

Provide your analysis in a structured JSON format that can be parsed programmatically.
```

---

## Prompt 2: Competitor Landscape Research

```
You are a competitive intelligence analyst researching the market landscape for a specific company.

TARGET COMPANY: {company_name}
INDUSTRY: {industry}
KNOWN COMPETITORS: {known_competitors}
WEBSITE: {website_url}

Conduct competitive landscape research and identify:

## 1. DIRECT COMPETITORS (Same product/service, same market)
For each competitor (identify 3-5):
- Company name
- Website
- Brief description
- Key products/services
- Apparent target market
- Pricing positioning (premium/mid/budget)
- Key differentiators
- Strengths (vs target company)
- Weaknesses (vs target company)

## 2. INDIRECT COMPETITORS (Alternative solutions)
- What alternatives exist to solve the same problem?
- DIY or manual alternatives
- Adjacent product categories

## 3. MARKET POSITIONING MAP
Describe where {company_name} fits on these dimensions:
- Price: Budget <-----> Premium
- Features: Simple <-----> Comprehensive
- Market: SMB <-----> Enterprise
- Approach: Traditional <-----> Innovative

## 4. COMPETITIVE ADVANTAGES
What unique advantages does {company_name} appear to have?

## 5. COMPETITIVE VULNERABILITIES
Where might {company_name} be vulnerable to competitors?

## 6. MARKET TRENDS
Key trends affecting this competitive landscape.

Return analysis in structured JSON format.
```

---

## Prompt 3: Content & Messaging Extraction

```
Analyze the following website content and extract key messaging elements.

WEBSITE CONTENT:
{raw_website_content}

Extract and categorize:

## 1. HEADLINES & HOOKS
- Main homepage headline
- Subheadlines
- Section headers
- CTA button text

## 2. BENEFIT STATEMENTS
List all benefit-focused statements found:
- Functional benefits (what it does)
- Emotional benefits (how it makes them feel)
- Social benefits (how it makes them look)

## 3. FEATURE DESCRIPTIONS
List all features mentioned with their descriptions.

## 4. SOCIAL PROOF ELEMENTS
- Testimonials (include full quotes)
- Statistics cited
- Customer logos
- Case study summaries

## 5. OBJECTION HANDLING
Any content that appears to address potential objections:
- Pricing concerns
- Implementation concerns
- Risk concerns
- Comparison to alternatives

## 6. BRAND PERSONALITY INDICATORS
Words and phrases that reveal brand personality.

## 7. KEYWORD THEMES
Frequently used words and phrases that indicate focus areas.

Return as structured JSON.
```

---

## Output Schema

```json
{
  "company_profile": {
    "name": "string",
    "legal_name": "string",
    "website": "string",
    "founded_year": "number",
    "headquarters": "string",
    "company_size": "string",
    "funding_status": "string",
    "leadership": [
      {
        "name": "string",
        "title": "string"
      }
    ],
    "mission_statement": "string",
    "vision_statement": "string"
  },
  "business_model": {
    "primary_model": "string",
    "customer_type": "B2B|B2C|Both",
    "target_segments": ["string"],
    "geographic_focus": ["string"],
    "pricing_strategy": "string"
  },
  "products_services": [
    {
      "name": "string",
      "description": "string",
      "features": ["string"],
      "target_user": "string",
      "pricing_tier": "string",
      "unique_aspects": ["string"]
    }
  ],
  "value_propositions": {
    "primary": "string",
    "secondary": ["string"],
    "proof_points": ["string"],
    "guarantees": ["string"]
  },
  "brand_voice": {
    "tone": "string",
    "complexity_level": "simple|moderate|technical",
    "themes": ["string"],
    "taglines": ["string"],
    "emotional_appeals": ["string"]
  },
  "target_audience_indicators": {
    "apparent_targets": ["string"],
    "industries": ["string"],
    "job_titles": ["string"],
    "company_sizes": ["string"],
    "pain_points_addressed": ["string"]
  },
  "competitive_positioning": {
    "positioning_statement": "string",
    "mentioned_competitors": ["string"],
    "claimed_differentiators": ["string"],
    "market_category": "string"
  },
  "trust_signals": {
    "testimonials": ["string"],
    "case_studies": ["string"],
    "awards": ["string"],
    "certifications": ["string"],
    "media_mentions": ["string"],
    "partnerships": ["string"]
  },
  "competitors": [
    {
      "name": "string",
      "website": "string",
      "description": "string",
      "key_products": ["string"],
      "target_market": "string",
      "pricing_position": "string",
      "differentiators": ["string"],
      "strengths_vs_target": ["string"],
      "weaknesses_vs_target": ["string"]
    }
  ]
}