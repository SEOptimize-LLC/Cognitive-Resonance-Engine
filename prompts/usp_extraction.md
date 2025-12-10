# USP Extraction Prompts - Value Proposition Canvas

## Prompt 1: Value Proposition Canvas Analysis

```
You are a strategic business consultant specializing in value proposition design using the Strategyzer Value Proposition Canvas framework.

Your task is to create a comprehensive Value Proposition Canvas that maps the company's offerings to a specific Ideal Customer Profile.

COMPANY PROFILE:
{company_profile_json}

TARGET ICP:
{icp_profile_json}

---

## PART 1: CUSTOMER PROFILE (Right Side of Canvas)

Analyze what this specific ICP needs, wants, and fears.

### 1.1 CUSTOMER JOBS

#### Functional Jobs (Tasks they're trying to accomplish)
For each job, rate importance (Critical / Important / Nice-to-have):

| Job Statement | Importance | Frequency | Context |
|--------------|------------|-----------|---------|
| "I need to..." | Critical/Important/Nice | Daily/Weekly/Monthly | When/where |

List 5-8 functional jobs:
1. [Job]: Importance, Frequency, Context
2. [Job]: Importance, Frequency, Context
...

#### Social Jobs (How they want to be perceived)
What image do they want to project? Who are they trying to impress?

| Social Job | Audience | Stakes |
|------------|----------|--------|
| "I want to be seen as..." | By whom | Why it matters |

List 3-5 social jobs:
1. [Job]: Audience, Stakes
2. [Job]: Audience, Stakes
...

#### Emotional Jobs (How they want to feel)
What emotional states are they seeking or avoiding?

| Emotional Job | Current State | Desired State |
|--------------|---------------|---------------|
| "I want to feel..." | How they feel now | Goal feeling |

List 3-5 emotional jobs:
1. [Job]: Current vs Desired state
2. [Job]: Current vs Desired state
...

### 1.2 PAINS

#### Functional Pains (What makes their job difficult)
| Pain | Severity (1-10) | Frequency | Impact |
|------|-----------------|-----------|--------|
| "It's frustrating that..." | X | Daily/Weekly/etc | Consequence |

Categories to cover:
- **Undesired outcomes**: Results they get but don't want
- **Obstacles**: What prevents them from starting or completing the job
- **Risks**: What could go wrong, potential negative consequences

List 8-12 pains ranked by severity:
1. [Pain]: Severity, Frequency, Impact
2. [Pain]: Severity, Frequency, Impact
...

#### Social Pains (Status/perception risks)
- What makes them look bad?
- What threatens their credibility?
- What social consequences do they fear?

#### Emotional Pains (Negative feelings)
- What frustrates them most?
- What causes anxiety?
- What makes them feel incompetent?

### 1.3 GAINS

#### Required Gains (Basic expectations - must have)
| Gain | Expectation Level | Without it... |
|------|------------------|---------------|
| "At minimum, I need..." | Baseline | Deal breaker if missing |

List 3-5 required gains:
1. [Gain]: Why it's required
2. [Gain]: Why it's required
...

#### Expected Gains (Typical expectations - should have)
| Gain | Common Alternatives | Expectation Source |
|------|--------------------|--------------------|
| "I expect to get..." | Current solutions offer this | Industry standard |

List 5-7 expected gains:
1. [Gain]: Industry context
2. [Gain]: Industry context
...

#### Desired Gains (Above expectations - could have)
| Gain | How it would help | Willingness to pay |
|------|-------------------|-------------------|
| "It would be great if..." | Impact on their life | Premium worthiness |

List 5-7 desired gains:
1. [Gain]: Impact, value
2. [Gain]: Impact, value
...

#### Unexpected Gains (Beyond imagination - wow factor)
| Gain | Surprise Element | Delight Factor |
|------|-----------------|----------------|
| "I never expected..." | Why surprising | Emotional impact |

List 2-3 unexpected gains:
1. [Gain]: Why it would delight
2. [Gain]: Why it would delight
...

---

## PART 2: VALUE MAP (Left Side of Canvas)

Map how the company's offering addresses the customer profile.

### 2.1 PRODUCTS & SERVICES

List all products, services, and supporting elements that help the ICP get their jobs done.

| Product/Service | Type | Description | Target Job |
|-----------------|------|-------------|------------|
| Name | Core/Supporting/Enabling | What it is | Which job it helps |

Categories:
- **Physical/Tangible**: Actual products
- **Intangible**: Services, warranties, support
- **Digital**: Software, content, data
- **Financial**: Pricing models, payment terms

List all relevant offerings:
1. [Product/Service]: Type, Description, Target Job
2. [Product/Service]: Type, Description, Target Job
...

### 2.2 PAIN RELIEVERS

For each significant customer pain, explain how the product/service addresses it.

| Customer Pain | Pain Reliever | Mechanism | Strength |
|---------------|--------------|-----------|----------|
| [Pain from 1.2] | How we address it | Specific feature/capability | Strong/Moderate/Weak |

**Pain Reliever Assessment:**
For each pain reliever, evaluate:
- **Directness**: Does it directly eliminate or just reduce the pain?
- **Completeness**: Does it fully address the pain or partially?
- **Proof**: What evidence supports this claim?
- **Uniqueness**: Do competitors offer the same relief?

Comprehensive mapping (cover all major pains):
1. **Pain**: [Customer pain statement]
   - **Reliever**: How we relieve it
   - **Mechanism**: Specific feature/approach
   - **Strength**: Strong/Moderate/Weak
   - **Evidence**: How we prove this
   - **Competitive Comparison**: How this compares to alternatives

2. [Continue for all major pains...]

### 2.3 GAIN CREATORS

For each significant customer gain, explain how the product/service creates it.

| Customer Gain | Gain Creator | Mechanism | Strength |
|---------------|-------------|-----------|----------|
| [Gain from 1.3] | How we create it | Specific feature/capability | Strong/Moderate/Weak |

**Gain Creator Assessment:**
For each gain creator, evaluate:
- **Relevance**: How important is this gain to the customer?
- **Magnitude**: How much gain do we create vs alternatives?
- **Proof**: What evidence supports this claim?
- **Uniqueness**: Do competitors create the same gains?

Comprehensive mapping:
1. **Gain**: [Customer gain statement]
   - **Creator**: How we create it
   - **Mechanism**: Specific feature/approach
   - **Strength**: Strong/Moderate/Weak
   - **Evidence**: How we prove this
   - **Competitive Comparison**: How this compares to alternatives

2. [Continue for all major gains...]

---

## PART 3: FIT ANALYSIS

### 3.1 FIT SCORE CALCULATION

Rate the alignment between Value Map and Customer Profile:

| Dimension | Score (1-10) | Justification |
|-----------|--------------|---------------|
| Job Fit | X | How well products address key jobs |
| Pain Fit | X | How well pain relievers address key pains |
| Gain Fit | X | How well gain creators deliver key gains |

**Overall Fit Score**: [Average of scores]

**Fit Level Classification:**
- 9-10: Problem-Solution Fit (Strong product-market fit)
- 7-8: Good Fit (Minor gaps)
- 5-6: Moderate Fit (Significant gaps to address)
- Below 5: Weak Fit (Major pivot needed)

### 3.2 FIT GAPS

#### Unaddressed Pains
Pains identified in customer profile that are not addressed:
| Pain | Severity | Gap Impact | Recommendation |
|------|----------|------------|----------------|
| [Pain] | X/10 | Business impact | How to address |

#### Uncreated Gains
Gains desired by customer that are not created:
| Gain | Importance | Gap Impact | Recommendation |
|------|------------|------------|----------------|
| [Gain] | Required/Expected/Desired | Business impact | How to address |

#### Over-Served Areas
Features/capabilities that exceed customer needs (potential bloat):
| Feature | Customer Need | Gap | Recommendation |
|---------|---------------|-----|----------------|
| [Feature] | Actual need level | Over-service degree | Simplify/Eliminate/Reposition |

### 3.3 UNIQUE DIFFERENTIATORS

Value elements that competitors cannot easily match:

| Differentiator | Why Unique | Defensibility | ICP Relevance |
|----------------|------------|---------------|---------------|
| [Element] | Why competitors can't match | How long it lasts | Why ICP cares |

List 3-5 true differentiators:
1. [Differentiator]: Explanation of uniqueness and value
2. [Differentiator]: Explanation
...

### 3.4 COMMODITY FEATURES

Value elements that all competitors offer (table stakes):

| Feature | Industry Standard | Our Performance | Importance |
|---------|------------------|-----------------|------------|
| [Feature] | What's expected | How we compare | Must-have vs nice-to-have |

List commodity features:
1. [Feature]: How we compare to standard
2. [Feature]: How we compare
...

---

## PART 4: STRATEGIC RECOMMENDATIONS

### 4.1 VALUE PROPOSITION STATEMENT

Craft positioning statements for this ICP:

**Full Value Proposition:**
"For [ICP description] who [key job or pain], [Company/Product] is a [category] that [key benefit]. Unlike [alternatives], we [key differentiator]."

**Short Version (10 words or less):**
[Concise value statement]

**Elevator Pitch (30 seconds):**
[Spoken version of full value prop]

### 4.2 MESSAGING HIERARCHY

**Primary Message** (Lead with this):
- Message:
- Supporting proof point:
- Emotional hook:

**Secondary Messages** (Reinforce with these):
1. Message | Proof | Hook
2. Message | Proof | Hook
3. Message | Proof | Hook

### 4.3 PROOF POINTS TO DEVELOP

Evidence needed to support value claims:
| Claim | Current Evidence | Needed Evidence | Priority |
|-------|-----------------|-----------------|----------|
| [Value claim] | What we have | What we need | High/Medium/Low |

---

Return the complete analysis as structured JSON following the schema below.
```

---

## Output Schema

```json
{
  "value_proposition_canvas": {
    "icp_id": "icp_1",
    "icp_name": "The Growth-Obsessed Startup Founder",
    
    "customer_profile": {
      "customer_jobs": {
        "functional_jobs": [
          {
            "job_statement": "Acquire customers efficiently at scale",
            "importance": "Critical",
            "frequency": "Daily",
            "context": "Growth is the primary success metric"
          }
        ],
        "social_jobs": [
          {
            "job_statement": "Be seen as a competent, visionary leader",
            "audience": "Investors, team, peers",
            "stakes": "Funding, talent attraction, credibility"
          }
        ],
        "emotional_jobs": [
          {
            "job_statement": "Feel in control of company trajectory",
            "current_state": "Overwhelmed by operational chaos",
            "desired_state": "Confident and strategic"
          }
        ]
      },
      "pains": {
        "functional_pains": [
          {
            "pain_statement": "Manual processes consume too much time",
            "severity": 9,
            "frequency": "Daily",
            "impact": "20+ hours/week lost to operational tasks",
            "category": "Obstacle"
          }
        ],
        "social_pains": [
          {
            "pain_statement": "Looking unprepared in investor meetings",
            "severity": 8,
            "trigger": "Board meetings, due diligence"
          }
        ],
        "emotional_pains": [
          {
            "pain_statement": "Anxiety about running out of runway",
            "severity": 9,
            "trigger": "Monthly burn rate review"
          }
        ]
      },
      "gains": {
        "required_gains": [
          {
            "gain_statement": "Must actually save time, not add complexity",
            "without_it": "Will abandon within first week"
          }
        ],
        "expected_gains": [
          {
            "gain_statement": "Clear ROI within 30 days",
            "industry_context": "Standard for SaaS tools"
          }
        ],
        "desired_gains": [
          {
            "gain_statement": "Insights that inform strategic decisions",
            "impact": "Better capital allocation, faster growth",
            "premium_worthy": true
          }
        ],
        "unexpected_gains": [
          {
            "gain_statement": "Automated reporting impresses investors",
            "surprise_factor": "Wasn't expecting polished deliverables",
            "delight_factor": "High - makes them look professional"
          }
        ]
      }
    },
    
    "value_map": {
      "products_services": [
        {
          "name": "Core Platform",
          "type": "Digital/Core",
          "description": "Main software solution",
          "target_jobs": ["Functional Job 1", "Functional Job 2"]
        }
      ],
      "pain_relievers": [
        {
          "customer_pain": "Manual processes consume too much time",
          "reliever": "Automated workflow engine",
          "mechanism": "AI-powered task automation",
          "strength": "Strong",
          "evidence": "Customers report 15+ hours saved weekly",
          "competitive_comparison": "Unique - competitors require manual setup"
        }
      ],
      "gain_creators": [
        {
          "customer_gain": "Clear ROI within 30 days",
          "creator": "ROI dashboard with automated tracking",
          "mechanism": "Integrates with tools to measure impact",
          "strength": "Strong",
          "evidence": "Case studies showing 3x ROI in first month",
          "competitive_comparison": "Most competitors don't offer ROI tracking"
        }
      ]
    },
    
    "fit_analysis": {
      "scores": {
        "job_fit": 8,
        "pain_fit": 9,
        "gain_fit": 7,
        "overall_fit": 8
      },
      "fit_level": "Good Fit",
      "unaddressed_pains": [
        {
          "pain": "Integration complexity with existing stack",
          "severity": 6,
          "gap_impact": "Medium - causes friction in adoption",
          "recommendation": "Develop more native integrations"
        }
      ],
      "uncreated_gains": [
        {
          "gain": "Team visibility and collaboration features",
          "importance": "Desired",
          "gap_impact": "Low - not critical but would enhance value",
          "recommendation": "Consider in product roadmap"
        }
      ],
      "over_served_areas": [],
      "unique_differentiators": [
        {
          "differentiator": "AI-powered automation that works on day one",
          "why_unique": "Competitors require weeks of setup",
          "defensibility": "High - based on proprietary ML models",
          "icp_relevance": "Critical - founders have no time for setup"
        }
      ],
      "commodity_features": [
        {
          "feature": "Basic reporting",
          "industry_standard": "All competitors offer this",
          "our_performance": "Par",
          "importance": "Table stakes"
        }
      ]
    },
    
    "strategic_recommendations": {
      "value_proposition_statements": {
        "full": "For growth-stage startup founders who are drowning in operational tasks, [Product] is an AI-powered automation platform that gives you back 15+ hours per week. Unlike tools that require weeks of setup, our system works on day one.",
        "short": "Reclaim your time. Scale your startup.",
        "elevator_pitch": "You know how startup founders spend half their time on tasks that don't grow the business? We've built an AI that automates all of that on day one - no setup, no learning curve. Our customers get back 15 hours a week to focus on what actually matters: growth."
      },
      "messaging_hierarchy": {
        "primary": {
          "message": "Get 15+ hours back every week",
          "proof_point": "Average time savings across 200+ startups",
          "emotional_hook": "Finally focus on growth, not operations"
        },
        "secondary": [
          {
            "message": "Works on day one",
            "proof_point": "Zero setup required",
            "emotional_hook": "No more implementation nightmares"
          }
        ]
      },
      "proof_points_needed": [
        {
          "claim": "15+ hours saved weekly",
          "current_evidence": "Customer surveys",
          "needed_evidence": "Time-tracking case study",
          "priority": "High"
        }
      ]
    }
  }
}
```

---

## Prompt 2: Competitive Differentiation Analysis

```
Analyze how the value proposition compares to competitive alternatives.

COMPANY VALUE MAP:
{value_map_json}

ICP PROFILE:
{icp_profile_json}

COMPETITIVE LANDSCAPE:
{competitors_json}

For each key competitor, analyze:

1. **Value Map Comparison**
   - Which customer jobs do they address?
   - How do their pain relievers compare?
   - How do their gain creators compare?

2. **Differentiation Matrix**
| Element | Our Offering | Competitor A | Competitor B | Our Advantage |
|---------|-------------|--------------|--------------|---------------|

3. **Positioning Opportunities**
   - Where can we own a unique position?
   - What should we never compete on?
   - What messaging will resonate vs fall flat?

Return analysis as structured JSON.