# Pain Point Taxonomy Prompts - JTBD Framework

## Prompt 1: Comprehensive Pain Point Analysis

```
You are an expert in Jobs-to-be-Done (JTBD) methodology, customer psychology, and pain point analysis.

Your task is to create a comprehensive Pain Point Taxonomy for a specific Ideal Customer Profile using the JTBD framework and Three-Dimensional Pain Categorization.

ICP PROFILE:
{icp_profile_json}

COMPANY PROFILE:
{company_profile_json}

VALUE PROPOSITION CANVAS:
{vpc_json}

---

## PART 1: THREE-DIMENSIONAL PAIN TAXONOMY

### 1.1 FUNCTIONAL PAIN POINTS (Process Friction)

Analyze pains related to the mechanics of getting jobs done.

#### Category: INEFFICIENCY
Pains related to time and speed:
| Pain Statement (Customer's Voice) | Severity (1-10) | Frequency | Time Impact | Current Workaround |
|-----------------------------------|-----------------|-----------|-------------|-------------------|
| "It takes too long to..." | X | Daily/Weekly/Monthly | Hours wasted | What they do now |

List 3-5 inefficiency pains:
1. **Pain**: [Statement]
   - Severity: X/10
   - Frequency: [How often]
   - Time Impact: [Hours/days lost]
   - Current Workaround: [How they cope]
   - Content Strategy: [How to address in marketing]

#### Category: COMPLEXITY
Pains related to difficulty and learning curve:
| Pain Statement | Severity | Barrier Type | Skill Gap |
|----------------|----------|--------------|-----------|
| "It's too difficult to..." | X | Technical/Process/Knowledge | What they lack |

List 3-5 complexity pains:
1. **Pain**: [Statement]
   - Severity: X/10
   - Barrier Type: [Technical/Process/Knowledge]
   - Skill Gap: [What they're missing]
   - Current Workaround: [How they cope]
   - Content Strategy: [How to address in marketing]

#### Category: INACCURACY
Pains related to errors and unreliable results:
| Pain Statement | Severity | Error Type | Consequence |
|----------------|----------|------------|-------------|
| "The results are often..." | X | Data/Process/Output | Impact of errors |

List 2-4 inaccuracy pains:
1. **Pain**: [Statement]
   - Severity: X/10
   - Error Type: [Data/Process/Output]
   - Consequence: [What happens when wrong]
   - Current Workaround: [How they verify]
   - Content Strategy: [How to address]

#### Category: INTEROPERABILITY
Pains related to integration and ecosystem:
| Pain Statement | Severity | Integration Gap | Data Silos |
|----------------|----------|-----------------|------------|
| "It doesn't work with..." | X | What won't connect | Trapped data |

List 2-3 interoperability pains:
1. **Pain**: [Statement]
   - Severity: X/10
   - Integration Gap: [What won't connect]
   - Data Impact: [Information trapped]
   - Current Workaround: [Manual bridges]
   - Content Strategy: [How to address]

#### Category: ACCESSIBILITY
Pains related to access and availability:
| Pain Statement | Severity | Access Barrier | When Blocked |
|----------------|----------|----------------|--------------|
| "I can't access it when..." | X | What prevents access | Critical moments |

List 2-3 accessibility pains:
1. **Pain**: [Statement]
   - Severity: X/10
   - Access Barrier: [What prevents access]
   - Critical Moments: [When access matters most]
   - Current Workaround: [Alternatives]
   - Content Strategy: [How to address]

---

### 1.2 FINANCIAL PAIN POINTS (Resource Friction)

Analyze pains related to economic costs and resource constraints.

#### Category: DIRECT COST
Pains related to explicit pricing:
| Pain Statement | Severity | Cost Type | Budget Impact |
|----------------|----------|-----------|---------------|
| "It's too expensive to..." | X | Subscription/License/Per-use | % of budget |

List 2-3 direct cost pains:
1. **Pain**: [Statement]
   - Severity: X/10
   - Cost Type: [Subscription/License/One-time/Per-use]
   - Budget Impact: [Percentage or dollar impact]
   - Price Threshold: [What they'd be willing to pay]
   - Content Strategy: [Value justification approach]

#### Category: HIDDEN COSTS
Pains related to unexpected expenses:
| Pain Statement | Severity | Hidden Cost Type | Discovery Point |
|----------------|----------|------------------|-----------------|
| "I didn't expect to also pay for..." | X | What cost is hidden | When discovered |

List 2-3 hidden cost pains:
1. **Pain**: [Statement]
   - Severity: X/10
   - Hidden Cost Type: [Implementation/Training/Maintenance/Add-ons]
   - Total Cost Impact: [Full cost picture]
   - Discovery Point: [When they realize]
   - Content Strategy: [Transparency approach]

#### Category: ROI UNCERTAINTY
Pains related to unclear returns:
| Pain Statement | Severity | Uncertainty Type | Decision Blocker |
|----------------|----------|------------------|------------------|
| "I'm not sure if..." | X | What's uncertain | Why they hesitate |

List 2-3 ROI uncertainty pains:
1. **Pain**: [Statement]
   - Severity: X/10
   - Uncertainty Type: [Payback time/Measurement difficulty/Value ambiguity]
   - Decision Blocker: [What prevents commitment]
   - Evidence Needed: [What would prove ROI]
   - Content Strategy: [Calculators/Case studies approach]

#### Category: CASH FLOW
Pains related to payment timing:
| Pain Statement | Severity | Cash Constraint | Budget Cycle |
|----------------|----------|-----------------|--------------|
| "We can't afford the upfront..." | X | Cash limitation | When budget frees |

List 1-2 cash flow pains:
1. **Pain**: [Statement]
   - Severity: X/10
   - Constraint: [Upfront cost/Annual prepay/Capital expense]
   - Budget Cycle: [When money available]
   - Content Strategy: [Pricing model flexibility]

#### Category: OPPORTUNITY COST
Pains related to alternative investments:
| Pain Statement | Severity | Alternative | Trade-off |
|----------------|----------|-------------|-----------|
| "Should I invest here or in..." | X | Other option | What they sacrifice |

List 1-2 opportunity cost pains:
1. **Pain**: [Statement]
   - Severity: X/10
   - Alternative: [What else they could invest in]
   - Trade-off: [What they give up]
   - Content Strategy: [Comparative value approach]

---

### 1.3 EMOTIONAL/PSYCHOLOGICAL PAIN POINTS (Internal Friction)

Analyze the deepest, often unspoken pains that drive behavior.

#### Category: ANXIETY
Pains related to fear and worry:
| Pain Statement | Severity | Root Fear | Trigger Situation |
|----------------|----------|-----------|-------------------|
| "I'm worried that..." | X | Deep fear | When it surfaces |

List 3-5 anxiety pains:
1. **Pain**: [Statement]
   - Severity: X/10
   - Root Fear: [What they're really afraid of]
   - Trigger Situations: [When this anxiety peaks]
   - Physical Manifestation: [How it shows - stress, avoidance]
   - Content Strategy: [Reassurance approach]

#### Category: FRUSTRATION
Pains related to anger and irritation:
| Pain Statement | Severity | Frustration Source | Emotional Toll |
|----------------|----------|-------------------|----------------|
| "I hate that I have to..." | X | What causes frustration | How it affects them |

List 3-5 frustration pains:
1. **Pain**: [Statement]
   - Severity: X/10
   - Source: [Repetition/Unfairness/Inefficiency/Lack of control]
   - Emotional Toll: [Burnout/Resentment/Disengagement]
   - Expression: [How they vent]
   - Content Strategy: [Validation + solution]

#### Category: OVERWHELM
Pains related to cognitive overload:
| Pain Statement | Severity | Overwhelm Type | Paralysis Effect |
|----------------|----------|----------------|------------------|
| "There's too much/many..." | X | Information/Options/Tasks | How they freeze |

List 2-3 overwhelm pains:
1. **Pain**: [Statement]
   - Severity: X/10
   - Type: [Information overload/Choice paralysis/Task mountain]
   - Paralysis Effect: [What they avoid/delay]
   - Coping Mechanism: [How they reduce]
   - Content Strategy: [Simplification approach]

#### Category: DISTRUST
Pains related to skepticism and doubt:
| Pain Statement | Severity | Trust Barrier | Past Experience |
|----------------|----------|---------------|-----------------|
| "I don't believe..." | X | What they doubt | What burned them |

List 2-3 distrust pains:
1. **Pain**: [Statement]
   - Severity: X/10
   - Trust Barrier: [Claims/Vendors/Technology]
   - Past Experience: [What created skepticism]
   - Trust Signals Needed: [What would build trust]
   - Content Strategy: [Credibility building]

#### Category: STATUS RISK
Pains related to reputation and perception:
| Pain Statement | Severity | Reputation Stakes | Audience |
|----------------|----------|-------------------|----------|
| "If this fails, I'll look..." | X | What's at risk | Who's watching |

List 2-3 status risk pains:
1. **Pain**: [Statement]
   - Severity: X/10
   - Stakes: [Job security/Credibility/Leadership image]
   - Audience: [Boss/Peers/Team/Board]
   - Protection Need: [How to save face]
   - Content Strategy: [Risk mitigation messaging]

---

## PART 2: JOBS-TO-BE-DONE FORCES ANALYSIS

### 2.1 THE FOUR FORCES OF PROGRESS

Analyze the forces that push customers toward or away from switching.

#### PUSH FACTORS (Pain of Status Quo)
What about their current situation is painful enough to drive change?

| Push Factor | Intensity (1-10) | Trend | Breaking Point |
|-------------|------------------|-------|----------------|
| "I can't keep..." | X | Getting worse/stable | When enough is enough |

List 5-7 push factors ranked by intensity:
1. **Factor**: [Statement]
   - Intensity: X/10
   - Trend: [Getting worse/Stable/Cyclical]
   - Breaking Point: [What would force action]
   - Messaging Angle: [How to amplify this push]

#### PULL FACTORS (Appeal of New Solution)
What about the new solution is attractive?

| Pull Factor | Intensity (1-10) | Benefit Type | Proof Required |
|-------------|------------------|--------------|----------------|
| "I want to be able to..." | X | Functional/Emotional/Social | What would prove it |

List 5-7 pull factors ranked by intensity:
1. **Factor**: [Statement]
   - Intensity: X/10
   - Benefit Type: [Functional/Emotional/Social]
   - Proof Required: [Demo/Testimonial/Trial]
   - Messaging Angle: [How to amplify this pull]

#### HABIT FACTORS (Inertia of Present)
What keeps them comfortable with the status quo?

| Habit Factor | Intensity (1-10) | Habit Type | Investment Sunk |
|--------------|------------------|------------|-----------------|
| "I've already..." | X | Behavioral/Investment/Relationship | What they'd lose |

List 4-6 habit factors ranked by intensity:
1. **Factor**: [Statement]
   - Intensity: X/10
   - Habit Type: [Behavioral/Financial Investment/Relationship/Knowledge]
   - Sunk Cost: [What they'd "lose"]
   - Neutralization: [How to reduce this force]

#### ANXIETY FACTORS (Fear of New)
What fears do they have about switching?

| Anxiety Factor | Intensity (1-10) | Fear Type | Worst Case |
|----------------|------------------|-----------|------------|
| "What if..." | X | Risk category | Scenario they fear |

List 4-6 anxiety factors ranked by intensity:
1. **Factor**: [Statement]
   - Intensity: X/10
   - Fear Type: [Implementation failure/Learning curve/Wrong choice/Switching cost]
   - Worst Case Scenario: [What they imagine going wrong]
   - Neutralization: [How to reduce this anxiety]

### 2.2 FORCE BALANCE ANALYSIS

Calculate the net force:
- Total Push Intensity: [Sum/10]
- Total Pull Intensity: [Sum/10]
- Total Habit Intensity: [Sum/10]
- Total Anxiety Intensity: [Sum/10]

**Net Force Calculation:**
(Push + Pull) - (Habit + Anxiety) = [Net Score]

**Interpretation:**
- Strong Positive (>15): High likelihood of switching
- Moderate Positive (5-15): Will switch with right trigger
- Neutral (-5 to 5): Needs significant push or pull increase
- Negative (<-5): Unlikely to switch without major change

**Current Assessment**: [Score and interpretation]

### 2.3 STRATEGIC RECOMMENDATIONS

Based on force analysis:

**Priority Focus Area**: [Which force to work on]
- If Push+Pull is weak: [How to increase attractiveness]
- If Habit+Anxiety is strong: [How to reduce barriers]

**Recommended Tactics**:
1. [Tactic]: [Specific action to shift forces]
2. [Tactic]: [Specific action]
3. [Tactic]: [Specific action]

---

## PART 3: FIVE WHYS ROOT CAUSE ANALYSIS

For the top 5 most severe pain points, conduct a "Five Whys" analysis.

### Pain Point 1: [Highest Severity Pain]

| Level | Question | Answer |
|-------|----------|--------|
| Surface | What is the problem? | [Stated pain] |
| Why 1 | Why is this a problem? | [First layer] |
| Why 2 | Why does that matter? | [Second layer] |
| Why 3 | Why is that important? | [Third layer] |
| Why 4 | Why do you care about that? | [Fourth layer] |
| Why 5 | What's the real fear/desire? | [Root cause] |

**Root Cause Identified**: [Deep motivation/fear]
**Marketing Implication**: [How to address in messaging]
**Content Angle**: [Specific content approach]

### Pain Point 2: [Second Severity Pain]
[Same structure...]

### Pain Point 3: [Third Severity Pain]
[Same structure...]

### Pain Point 4: [Fourth Severity Pain]
[Same structure...]

### Pain Point 5: [Fifth Severity Pain]
[Same structure...]

---

## PART 4: PAIN POINT TO CONTENT MAPPING

### 4.1 CONTENT STRATEGY BY PAIN CATEGORY

#### Functional Pains → Logic-Based Content
| Pain | Content Type | Content Topic | Format | Funnel Stage |
|------|--------------|---------------|--------|--------------|
| [Pain] | Demonstration | [Topic] | Video/Article | Evaluation |

#### Financial Pains → ROI-Based Content
| Pain | Content Type | Content Topic | Format | Funnel Stage |
|------|--------------|---------------|--------|--------------|
| [Pain] | Calculator/Case Study | [Topic] | Interactive/PDF | Evaluation |

#### Emotional Pains → Empathy-Based Content
| Pain | Content Type | Content Topic | Format | Funnel Stage |
|------|--------------|---------------|--------|--------------|
| [Pain] | Story/Testimonial | [Topic] | Video/Article | Trigger/Evaluation |

### 4.2 OBJECTION HANDLING CONTENT MATRIX

For each major anxiety/objection:
| Objection | Content Response | Format | Placement |
|-----------|------------------|--------|-----------|
| "What if..." | [Response approach] | FAQ/Video/Article | Where to deploy |

---

Return the complete analysis as structured JSON following the schema provided.
```

---

## Output Schema

```json
{
  "pain_point_taxonomy": {
    "icp_id": "icp_1",
    "icp_name": "The Growth-Obsessed Startup Founder",
    
    "functional_pains": {
      "inefficiency": [
        {
          "pain_statement": "I spend 10+ hours weekly on manual data entry",
          "severity": 9,
          "frequency": "Daily",
          "time_impact": "10-15 hours/week",
          "current_workaround": "Hiring VAs, batch processing on weekends",
          "content_strategy": "Show time-savings calculator, before/after demos"
        }
      ],
      "complexity": [],
      "inaccuracy": [],
      "interoperability": [],
      "accessibility": []
    },
    
    "financial_pains": {
      "direct_cost": [],
      "hidden_costs": [],
      "roi_uncertainty": [],
      "cash_flow": [],
      "opportunity_cost": []
    },
    
    "emotional_pains": {
      "anxiety": [
        {
          "pain_statement": "I'm terrified we'll miss our growth window",
          "severity": 9,
          "root_fear": "Company failure, letting down team and investors",
          "trigger_situations": ["Slow growth months", "Competitor funding news", "Board meetings"],
          "physical_manifestation": "Sleep problems, irritability, avoidance of metrics",
          "content_strategy": "Success stories of similar-stage startups, risk mitigation messaging"
        }
      ],
      "frustration": [],
      "overwhelm": [],
      "distrust": [],
      "status_risk": []
    },
    
    "forces_analysis": {
      "push_factors": [
        {
          "factor": "Current tools require too much manual work",
          "intensity": 8,
          "trend": "Getting worse as we scale",
          "breaking_point": "Next hire would be just for data management",
          "messaging_angle": "Before you hire another person to manage spreadsheets..."
        }
      ],
      "pull_factors": [
        {
          "factor": "Automation would free me to focus on strategy",
          "intensity": 9,
          "benefit_type": "Functional + Emotional",
          "proof_required": "Demo showing actual time saved",
          "messaging_angle": "Imagine getting 15 hours back every week"
        }
      ],
      "habit_factors": [
        {
          "factor": "We've already built workflows around current tools",
          "intensity": 6,
          "habit_type": "Behavioral + Financial Investment",
          "sunk_cost": "3 months of setup, team training",
          "neutralization": "Show migration is painless, workflows can transfer"
        }
      ],
      "anxiety_factors": [
        {
          "factor": "What if my team doesn't adopt it?",
          "intensity": 7,
          "fear_type": "Implementation failure",
          "worst_case_scenario": "Wasted money, lost time, look bad to team",
          "neutralization": "Team adoption guarantee, onboarding support, success metrics"
        }
      ],
      "force_balance": {
        "total_push": 32,
        "total_pull": 38,
        "total_habit": 24,
        "total_anxiety": 28,
        "net_force": 18,
        "assessment": "Moderate Positive - Will switch with right trigger",
        "recommendation": "Focus on reducing anxiety through guarantees and proof"
      }
    },
    
    "five_whys_analysis": [
      {
        "pain_point": "I spend too much time on manual data entry",
        "surface": "10+ hours weekly on data entry",
        "why_1": "Because our tools don't talk to each other",
        "why_2": "Because I need complete data for decision-making",
        "why_3": "Because wrong decisions could kill the company",
        "why_4": "Because I'm responsible for our success or failure",
        "why_5": "Because my identity is tied to this company's outcome",
        "root_cause": "Identity and self-worth tied to company success",
        "marketing_implication": "Position as tool that protects their legacy",
        "content_angle": "How successful founders protect their time and focus"
      }
    ],
    
    "content_mapping": {
      "functional_pain_content": [
        {
          "pain": "Manual data entry time",
          "content_type": "Demonstration",
          "topic": "Watch us automate a 2-hour task in 2 minutes",
          "format": "Video walkthrough",
          "funnel_stage": "Evaluation"
        }
      ],
      "financial_pain_content": [],
      "emotional_pain_content": [],
      "objection_handling": [
        {
          "objection": "What if my team doesn't adopt it?",
          "response_approach": "Team adoption success stories + guarantee",
          "format": "Case study + policy page",
          "placement": "Pricing page, sales calls"
        }
      ]
    },
    
    "switching_analysis": {
      "switching_barriers": [
        "Existing workflow dependencies",
        "Team retraining costs",
        "Data migration concerns"
      ],
      "switching_triggers": [
        "Hiring decision that would exist just for manual work",
        "Major error caused by manual process",
        "Competitor leap ahead due to better tools",
        "Investor pressure on operational efficiency"
      ]
    }
  }
}