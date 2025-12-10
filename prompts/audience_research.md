# Audience Research Prompts - ICP Generation

## Prompt 1: ICP Identification & Segmentation

```
You are an expert market researcher and customer strategist specializing in customer segmentation, psychographic analysis, and buyer persona development.

Based on the following company profile, generate comprehensive Ideal Customer Profiles (ICPs).

COMPANY PROFILE:
{company_profile_json}

INSTRUCTIONS:
Generate {num_icps} distinct Ideal Customer Profiles for this business. Each ICP should represent a meaningfully different segment with unique characteristics, motivations, and needs.

For each ICP, provide the following comprehensive analysis:

---

## ICP {n}: [MEMORABLE DESCRIPTIVE NAME]
Example names: "The Growth-Obsessed Startup Founder", "The Risk-Averse Enterprise Buyer", "The Efficiency-Driven Operations Manager"

### 1. SEGMENT OVERVIEW
- **One-Liner Description**: A single sentence capturing the essence of this persona
- **Segment Priority**: Primary / Secondary / Niche
- **Estimated Segment Size**: Large / Medium / Small
- **Revenue Potential**: High / Medium / Low
- **Acquisition Difficulty**: Easy / Moderate / Difficult

### 2. DEMOGRAPHICS / FIRMOGRAPHICS

#### For B2B:
- **Company Size**: Employee count range
- **Annual Revenue**: Revenue range
- **Industry Verticals**: Primary industries
- **Company Stage**: Startup / Growth / Mature / Enterprise
- **Department**: Which department owns the budget
- **Geographic Focus**: Regions/countries

#### Key Decision Makers:
| Role | Title Examples | Influence Level | Key Concerns |
|------|---------------|-----------------|--------------|
| Economic Buyer | CFO, VP Finance | Final approval | ROI, budget |
| Technical Buyer | CTO, IT Director | Veto power | Integration, security |
| User Buyer | Manager, Team Lead | Daily champion | Ease of use |
| Champion | Various | Internal advocate | Career advancement |

#### For B2C:
- **Age Range**: X-Y years
- **Gender Skew**: If any
- **Income Bracket**: Annual household income
- **Education Level**: Typical education
- **Family Status**: Single / Married / Children
- **Location Type**: Urban / Suburban / Rural
- **Geographic Focus**: Regions

### 3. PSYCHOGRAPHICS

#### Core Values (Rank top 5)
1. [Value] - Why this matters to them
2. [Value] - Why this matters to them
3. [Value] - Why this matters to them
4. [Value] - Why this matters to them
5. [Value] - Why this matters to them

#### Aspirations & Goals
**Professional/Functional Aspirations:**
- What they want to achieve
- Where they want to be in 2-3 years
- What success looks like to them

**Personal/Emotional Aspirations:**
- How they want to feel
- How they want to be perceived
- Status or identity goals

#### Decision-Making Style
- **Type**: Analytical / Intuitive / Collaborative / Decisive
- **Research Depth**: Light / Moderate / Extensive
- **Risk Tolerance**: Risk-Averse / Moderate / Risk-Seeking
- **Speed**: Quick decisions / Deliberate process
- **Influences**: Data-driven / Peer-influenced / Expert-influenced / Emotionally-driven

#### Big Five Personality Indicators (Estimated)
| Trait | Level | Behavioral Implication |
|-------|-------|----------------------|
| Openness | High/Med/Low | How they respond to innovation |
| Conscientiousness | High/Med/Low | Detail orientation, planning |
| Extraversion | High/Med/Low | Communication preferences |
| Agreeableness | High/Med/Low | Negotiation style |
| Neuroticism | High/Med/Low | Risk sensitivity |

### 4. BEHAVIORAL PROFILE

#### Information Consumption
- **Preferred Channels**: Where they seek information
- **Content Formats**: What format they prefer (video/text/audio/interactive)
- **Trusted Sources**: Who/what they trust for recommendations
- **Research Behavior**: How they research before buying
- **Social Platforms**: Which platforms they use professionally

#### Buying Behavior
- **Buying Cycle Length**: Days / Weeks / Months
- **Typical Research Steps**: Step-by-step process
- **Key Evaluation Criteria**: What they compare
- **Deal Breakers**: What makes them walk away
- **Price Sensitivity**: High / Medium / Low

#### Technology Adoption
- **Adoption Curve Position**: Innovator / Early Adopter / Early Majority / Late Majority / Laggard
- **Technical Sophistication**: High / Medium / Low
- **Tool Stack Indicators**: What tools they likely use

### 5. TRIGGERS - MOTIVATIONS

#### Primary Motivations (Top 3-5)
For each motivation:
| Motivation | Type | Intensity | Trigger Event |
|------------|------|-----------|---------------|
| [Statement] | Internal/External | High/Med/Low | What triggers this |

**Internal Motivations** (Personal gains):
1. [Motivation]: Detailed explanation of why this drives them
2. [Motivation]: Detailed explanation
3. [Motivation]: Detailed explanation

**External Motivations** (Business/Social pressures):
1. [Motivation]: Detailed explanation
2. [Motivation]: Detailed explanation
3. [Motivation]: Detailed explanation

### 6. TRIGGERS - PAIN POINTS

#### Functional Pain Points
| Pain Point | Severity (1-10) | Frequency | Current Workaround |
|------------|-----------------|-----------|-------------------|
| Statement in their voice | X | Daily/Weekly/Monthly | What they do now |

1. **[Pain Point]**: 
   - *Severity*: X/10
   - *In their words*: "Quote-style statement"
   - *Current workaround*: How they cope
   - *Cost of this pain*: Time/money/opportunity

#### Financial Pain Points
| Pain Point | Impact | Evidence |
|------------|--------|----------|
| Statement | Dollar/time impact | How we know |

#### Emotional Pain Points
| Pain Point | Underlying Fear | Trigger Situation |
|------------|-----------------|-------------------|
| Statement | What they're really afraid of | When this surfaces |

### 7. GOALS

#### Immediate Goals (Next 3-6 months)
1. [Goal]: Why this matters now
2. [Goal]: Why this matters now
3. [Goal]: Why this matters now

#### Long-term Goals (1-3 years)
1. [Goal]: How they measure success
2. [Goal]: How they measure success

#### Success Metrics They Care About
- Metric 1: Why this matters
- Metric 2: Why this matters
- Metric 3: Why this matters

### 8. FEARS & OBJECTIONS

#### Deep Fears
1. **[Fear]**: The underlying anxiety and what triggers it
2. **[Fear]**: The underlying anxiety and what triggers it

#### Likely Objections to {company_name}
| Objection | Root Cause | Counter-Strategy |
|-----------|------------|-----------------|
| "Statement" | Why they think this | How to address |

#### Risk Concerns
- What could go wrong in their mind
- Consequences they want to avoid
- Who they'd have to answer to

### 9. MESSAGING HOOKS

#### Resonant Themes
- Theme 1: Why this resonates with this ICP
- Theme 2: Why this resonates with this ICP
- Theme 3: Why this resonates with this ICP

#### Language Patterns
- Words/phrases that would appeal to them
- Jargon they use and understand
- Tone that would feel trustworthy

#### Emotional Triggers
- What emotional states drive their action
- Stories/scenarios that would capture attention

### 10. DETAILED NARRATIVE

Write a 2-3 paragraph narrative portrait of this ICP. Include:
- A day in their life
- Their current struggles
- What would make their life better
- How they would discover and evaluate a solution like {company_name}

---

Return all ICPs in a structured JSON format following the schema below.
```

---

## Output Schema

```json
{
  "icps": [
    {
      "icp_id": "icp_1",
      "icp_name": "The Growth-Obsessed Startup Founder",
      "one_liner": "Early-stage founders who prioritize speed and scalability over everything else",
      "segment_priority": "Primary",
      "segment_size": "Medium",
      "revenue_potential": "High",
      "acquisition_difficulty": "Moderate",
      
      "demographics": {
        "customer_type": "B2B",
        "company_size": "1-50 employees",
        "annual_revenue": "$500K - $10M",
        "industry_verticals": ["SaaS", "Fintech", "E-commerce"],
        "company_stage": "Startup/Growth",
        "department": "Executive/Operations",
        "geographic_focus": ["North America", "Western Europe"],
        "decision_makers": [
          {
            "role": "Economic Buyer",
            "title_examples": ["CEO", "Founder", "COO"],
            "influence_level": "Final approval",
            "key_concerns": ["ROI", "Speed to value", "Scalability"]
          }
        ]
      },
      
      "psychographics": {
        "core_values": [
          {"value": "Speed", "importance": "Highest", "reason": "Time is their scarcest resource"},
          {"value": "Innovation", "importance": "High", "reason": "Competitive differentiation"},
          {"value": "Efficiency", "importance": "High", "reason": "Must do more with less"},
          {"value": "Growth", "importance": "High", "reason": "Measure of success"},
          {"value": "Independence", "importance": "Medium", "reason": "Control over destiny"}
        ],
        "aspirations": {
          "professional": ["Scale company 10x", "Raise next funding round", "Dominate market niche"],
          "personal": ["Be recognized as industry leader", "Build lasting company", "Achieve financial freedom"]
        },
        "decision_style": {
          "type": "Decisive",
          "research_depth": "Moderate",
          "risk_tolerance": "Risk-Seeking",
          "speed": "Quick decisions",
          "primary_influence": "Peer-influenced"
        },
        "big_five_indicators": {
          "openness": {"level": "High", "implication": "Receptive to new solutions"},
          "conscientiousness": {"level": "Medium", "implication": "Values efficiency over perfection"},
          "extraversion": {"level": "High", "implication": "Engages on social, attends events"},
          "agreeableness": {"level": "Medium", "implication": "Tough negotiator but fair"},
          "neuroticism": {"level": "Medium", "implication": "Some anxiety about failure"}
        }
      },
      
      "behavioral": {
        "information_consumption": {
          "preferred_channels": ["Twitter/X", "LinkedIn", "Podcasts", "Founder communities"],
          "content_formats": ["Short-form video", "Podcasts", "Twitter threads"],
          "trusted_sources": ["Other founders", "VCs", "Tech journalists"],
          "research_behavior": "Quick scan, peer validation, then trial",
          "social_platforms": ["Twitter/X", "LinkedIn"]
        },
        "buying_behavior": {
          "cycle_length": "Days to weeks",
          "research_steps": ["Peer recommendation", "Quick demo", "Free trial", "Decision"],
          "evaluation_criteria": ["Speed of implementation", "ROI clarity", "Integration ease"],
          "deal_breakers": ["Long sales cycles", "Heavy implementation", "Unclear pricing"],
          "price_sensitivity": "Low if value is clear"
        },
        "technology_adoption": {
          "curve_position": "Early Adopter",
          "technical_sophistication": "High",
          "tool_stack_indicators": ["Modern SaaS stack", "Cloud-native", "API-first tools"]
        }
      },
      
      "motivations": {
        "internal": [
          {"motivation": "Prove concept works at scale", "intensity": "High", "trigger": "Hitting growth ceiling"},
          {"motivation": "Free up time from operations", "intensity": "High", "trigger": "Working 80+ hour weeks"},
          {"motivation": "Feel in control of trajectory", "intensity": "Medium", "trigger": "Uncertainty about path"}
        ],
        "external": [
          {"motivation": "Meet investor expectations", "intensity": "High", "trigger": "Board meetings, runway concerns"},
          {"motivation": "Outpace competitors", "intensity": "High", "trigger": "Competitor announcements"},
          {"motivation": "Attract top talent", "intensity": "Medium", "trigger": "Failed hires, scaling team"}
        ]
      },
      
      "pain_points": {
        "functional": [
          {
            "statement": "I spend too much time on tasks that should be automated",
            "severity": 8,
            "frequency": "Daily",
            "current_workaround": "Hiring VAs, manual processes",
            "cost": "20+ hours/week of founder time"
          }
        ],
        "financial": [
          {
            "statement": "I'm not sure which investments will actually drive growth",
            "impact": "Potential wasted spend of 20-30% of budget",
            "evidence": "Multiple failed tool subscriptions"
          }
        ],
        "emotional": [
          {
            "statement": "I'm afraid we'll miss our growth window",
            "underlying_fear": "Company failure, letting down team/investors",
            "trigger_situation": "Slow months, competitor wins"
          }
        ]
      },
      
      "goals": {
        "immediate": [
          {"goal": "Increase MRR by 50%", "reason": "Runway extension, investor metrics"},
          {"goal": "Reduce operational overhead", "reason": "Focus on strategic work"},
          {"goal": "Improve team productivity", "reason": "Do more with current headcount"}
        ],
        "long_term": [
          {"goal": "Reach Series A/B milestone", "success_metric": "Revenue target, growth rate"},
          {"goal": "Become market category leader", "success_metric": "Market share, recognition"}
        ],
        "success_metrics": ["MRR growth rate", "Customer acquisition cost", "Time to value"]
      },
      
      "fears": {
        "deep_fears": [
          {"fear": "Running out of runway before finding PMF", "trigger": "Cash burn rate discussions"},
          {"fear": "Being disrupted by faster competitor", "trigger": "Competitor funding announcements"}
        ],
        "likely_objections": [
          {
            "objection": "I don't have time to implement another tool",
            "root_cause": "Past implementation failures, time scarcity",
            "counter_strategy": "Emphasize speed to value, done-for-you onboarding"
          }
        ],
        "risk_concerns": ["Wasting limited resources", "Team adoption failure", "Distraction from core business"]
      },
      
      "messaging_hooks": {
        "resonant_themes": ["Speed to results", "10x efficiency", "Founder-tested"],
        "language_patterns": ["Scale", "Automate", "Growth", "Efficiency", "ROI"],
        "emotional_triggers": ["FOMO on growth", "Peer success stories", "Time freedom"]
      },
      
      "narrative": "Meet Alex, a 32-year-old founder of a B2B SaaS startup that just closed their seed round. They wake up at 6 AM already behind on emails, spending the first two hours of their day on operational tasks that feel urgent but aren't strategic. Their calendar is a wall of meetings, and the actual 'founder work'—product vision, customer conversations, fundraising prep—gets pushed to evenings and weekends.\n\nWhat keeps Alex up at night is the burn rate clock. Every month without hitting growth targets is a month closer to a difficult conversation with investors. They've tried several tools promising to save time, but most required weeks of setup and never got fully adopted by the team. What Alex needs isn't another feature-rich platform—it's something that works on day one, proves ROI by day seven, and becomes invisible by day thirty.\n\nWhen Alex hears about a new solution, they first check Twitter to see if anyone they respect is using it. They'll watch a 2-minute demo video, and if it looks promising, they'll sign up for a free trial during a meeting that's running slow. The decision to buy happens fast if the trial shows immediate value—but abandonment is equally fast if setup takes more than an hour."
    }
  ]
}
```

---

## Prompt 2: ICP Validation & Refinement

```
You are a market research expert reviewing and refining Ideal Customer Profiles.

COMPANY PROFILE:
{company_profile_json}

DRAFT ICPs:
{draft_icps_json}

Review each ICP for:

1. **Internal Consistency**
   - Do the psychographics align with the behavioral patterns?
   - Are the pain points consistent with the motivations?
   - Does the decision-making style match the buying behavior?

2. **Differentiation**
   - Are the ICPs meaningfully different from each other?
   - Is there clear value in targeting each separately?
   - Could any be combined or split?

3. **Actionability**
   - Can marketing actually reach this ICP with available channels?
   - Are the messaging hooks specific enough to create content?
   - Are the pain points concrete enough to address?

4. **Company Fit**
   - Does this ICP match what the company actually offers?
   - Can the company's solution genuinely address the pain points?
   - Is the ICP's budget aligned with the company's pricing?

For each ICP, provide:
- Confidence score (1-10)
- Identified gaps or inconsistencies
- Suggested refinements
- Priority ranking recommendation

Return as structured JSON.