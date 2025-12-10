# Customer Journey Mapping Prompts - 5-Stage Model

## Framework Overview

The 5-stage customer journey model provides better granularity for campaign planning:

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                           CUSTOMER JOURNEY - 5 STAGES                           │
├─────────────────────────────────────────────────────────────────────────────────┤
│                                                                                 │
│   PRE-PURCHASE                                      POST-PURCHASE               │
│   ┌───────────────────────────────────────┐  ┌────────────────────────────┐    │
│   │                                       │  │                            │    │
│   │  ┌──────────┐  ┌─────────────────┐   │  │  ┌───────────┐  ┌────────┐ │    │
│   │  │ AWARENESS│─►│ CONSIDERATION   │───┼──┼─►│ ONBOARDING│─►│EXPANSION│ │    │
│   │  │          │  │                 │   │  │  │           │  │        │ │    │
│   │  │ Problem  │  │ Solution        │   │  │  │ First     │  │Retention│ │    │
│   │  │ Recognition│ │ Research       │   │  │  │ Value     │  │Advocacy │ │    │
│   │  └──────────┘  └─────────────────┘   │  │  └───────────┘  └────────┘ │    │
│   │                         │            │  │                            │    │
│   │                         ▼            │  │                            │    │
│   │              ┌──────────────────┐    │  │                            │    │
│   │              │    DECISION      │────┼──┘                            │    │
│   │              │                  │    │                               │    │
│   │              │ Vendor Selection │    │                               │    │
│   │              │ Purchase         │    │                               │    │
│   │              └──────────────────┘    │                               │    │
│   │                                      │                               │    │
│   └──────────────────────────────────────┘  └────────────────────────────┘    │
│                                                                                 │
└─────────────────────────────────────────────────────────────────────────────────┘
```

### Stage Ownership & Content Focus

| Stage | Primary Owner | Customer Question | Content Focus |
|-------|---------------|-------------------|---------------|
| **Awareness** | Marketing | "What's causing this problem?" | Pain education, symptom validation |
| **Consideration** | Marketing | "What solutions exist?" | Solution comparison, category education |
| **Decision** | Sales + Marketing | "Which vendor is best for me?" | Proof, demos, objection handling |
| **Onboarding** | Customer Success | "How do I get started?" | Quick wins, training |
| **Expansion** | CS + Marketing | "How can I get more value?" | Advanced features, referrals, upsells |

---

## Prompt 1: Comprehensive 5-Stage Journey Map

```
You are a customer journey strategist and marketing funnel expert specializing in B2B and B2C customer experience design.

Create a comprehensive 5-stage Customer Journey Map for the following Ideal Customer Profile. This map will be used directly by a marketing team to plan content marketing and paid advertising campaigns.

---

## INPUT DATA

ICP PROFILE:
{icp_profile}

PAIN POINT TAXONOMY:
{pain_points}

VALUE PROPOSITION CANVAS:
{vpc}

COMPANY PROFILE:
{company_profile}

---

## JOURNEY MAP FOR: {icp_name}

Provide a complete journey map covering all 5 stages with actionable detail for campaign planning.

---

# STAGE 1: AWARENESS

## Stage Context

**Objective**: Move prospect from "Unaware" or "Problem Aware" to "Solution Aware"

**Where They Are**:
- Starting awareness level (Unaware of problem / Aware of symptoms / Aware of problem but not solutions)
- Primary emotional state (Frustration / Confusion / Curiosity / Denial)
- Urgency level (Low / Emerging / Moderate)
- Information-seeking behavior (Passive / Beginning to search)

**Trigger Events** - What prompts them to start their journey:
List 5-7 specific events or moments that would trigger awareness:
1. [Event]: Brief description and why it triggers search
2. [Event]: Brief description
3. [Event]: Brief description
(continue...)

## Questions They're Asking

**Internal Questions** (thinking to themselves):
- "Why is [symptom] happening?"
- "Is this normal or is something wrong?"
- "Am I the only one dealing with this?"
(list 5-7 questions)

**Search Queries** (what they type into Google):
| Query | Search Intent | Content Opportunity |
|-------|---------------|---------------------|
| "[symptom] causes" | Understanding problem | Blog post |
| "why does [problem] happen" | Root cause | Educational guide |
(list 8-10 queries)

## Information Needs

What information do they need at this stage?

1. **Problem Validation**: Confirmation that their experience is real and shared by others
2. **Root Cause Education**: Understanding why the problem exists
3. **Impact Awareness**: Understanding the true cost of the problem
4. **Solution Categories**: What types of solutions exist (not specific vendors)
(list 5-7 needs with explanations)

## Channel Preferences

Where are they looking for information?

**Primary Channels** (highest influence):
| Channel | Why They Use It | Content That Works | Trust Level |
|---------|-----------------|-------------------|-------------|
| [Channel] | [Reason] | [Format/style] | High/Medium/Low |

**Secondary Channels**:
| Channel | Usage Context | Content That Works |
|---------|---------------|-------------------|
| [Channel] | [When/why] | [Format/style] |

**Influencers They Trust**:
- [Type of person/source]: Why trusted at this stage
(list 3-5 influencer types)

## Content Strategy

### Content Themes That Resonate
| Theme | Why It Resonates | Angle/Approach |
|-------|------------------|----------------|
| "[Theme]" | Connection to their experience | How to approach |
(list 5-7 themes)

### Recommended Content Formats
| Format | Effectiveness | Best For | Example |
|--------|--------------|----------|---------|
| [Format] | High/Medium | [Purpose] | [Topic example] |
(list 5-7 formats ranked by effectiveness)

### Content Ideas - Detailed
Provide 15+ specific content ideas:

**Blog Posts/Articles**:
1. **"[Title]"**
   - Hook: [Opening that grabs attention]
   - Key Sections: [Outline]
   - CTA: [Next step]

2. **"[Title]"**
   - Hook: [Opening]
   - Key Sections: [Outline]
   - CTA: [Next step]
(provide 5-7 blog ideas)

**Video Content**:
1. **"[Title]"**
   - Format: [Short-form/Long-form, style]
   - Hook: [First 3 seconds]
   - Key Message: [Core takeaway]
(provide 3-5 video ideas)

**Interactive Content**:
1. **"[Assessment/Quiz Name]"**
   - Value to User: What they learn about themselves
   - Sample Questions: 3-4 example questions
   - Output: What result they get
   - Data Captured: What you learn for segmentation
(provide 2-3 interactive content ideas)

**Social Media Content**:
1. **[Platform]: "[Post concept]"**
   - Format: [Carousel/Thread/Short video]
   - Hook: [Opening]
(provide 3-5 social content ideas)

## Paid Advertising Strategy

### Campaign Objective
[Awareness / Traffic / Lead Generation]

### Platform Mix
| Platform | Budget % | Objective | Why This Platform |
|----------|----------|-----------|-------------------|
| [Platform] | X% | [Goal] | [Reason for this ICP] |

### Targeting Approach
**Interest-Based Targeting**:
- [Interest 1]: Why relevant
- [Interest 2]: Why relevant
(list 5-7 interests)

**Behavioral Targeting**:
- [Behavior]: Why indicative
(list 3-5 behaviors)

**Lookalike Audiences**:
- Seed: [What audience to base on]
- Size: [Recommended %]

**Contextual/Placement Targeting**:
- [Site/context type]: Why they'd be there
(list 3-5 placements)

### Ad Creative Directions
Provide 4-5 distinct creative angles to test:

**Angle 1: Pain Validation**
- Headline: "[Example headline]"
- Body Copy Direction: [Approach]
- Emotional Trigger: [What emotion]
- Visual Direction: [Image/video concept]

**Angle 2: Curiosity Gap**
- Headline: "[Example headline]"
- Body Copy Direction: [Approach]
- Emotional Trigger: [What emotion]
- Visual Direction: [Image/video concept]

**Angle 3: Social Proof / Peer Reference**
- Headline: "[Example headline]"
- Body Copy Direction: [Approach]
- Emotional Trigger: [What emotion]
- Visual Direction: [Image/video concept]

**Angle 4: Myth-Buster / Contrarian**
- Headline: "[Example headline]"
- Body Copy Direction: [Approach]
- Emotional Trigger: [What emotion]
- Visual Direction: [Image/video concept]

(Add additional angles as relevant)

### Retargeting Setup
- **Audience to Create**: [Who engaged with awareness content]
- **Pixel Events**: [What to track]
- **Audience Duration**: [How long to keep in audience]

## Success Metrics

| KPI | Target | Measurement Method |
|-----|--------|-------------------|
| [Metric] | [Target] | [How to measure] |

**Primary KPIs**:
1. [Metric]: Why it matters, target
2. [Metric]: Why it matters, target

**Stage Completion Signal**: [What behavior indicates they're ready for Consideration]

---

# STAGE 2: CONSIDERATION

## Stage Context

**Objective**: Move prospect from "Solution Aware" to "Product Aware" (knows specific vendors/options)

**Where They Are**:
- Knows the problem has solutions
- Researching *types* of solutions (not comparing vendors yet)
- Building mental model of solution category
- May be building internal case for change

**What's Changed From Awareness**:
- Now actively searching for solutions (not just information)
- Willing to provide contact info for valuable content
- Starting to form preferences about solution approach

## Questions They're Asking

**Solution Category Questions**:
- "What are the different ways to solve [problem]?"
- "What's the difference between [approach A] vs [approach B]?"
- "What should I look for in a [solution category]?"
(list 7-10 questions)

**Search Queries**:
| Query | Intent | Content Opportunity |
|-------|--------|---------------------|
| "best [solution type] for [use case]" | Solution research | Comparison guide |
| "[solution A] vs [solution B]" | Approach comparison | Versus article |
| "how to choose [solution type]" | Evaluation framework | Buyer's guide |
(list 10-12 queries)

## Information Needs

1. **Solution Education**: Understanding how different approaches work
2. **Evaluation Criteria**: Framework for comparing options
3. **Fit Assessment**: Which approach is right for their situation
4. **Effort/Investment Preview**: What implementing a solution requires
(list 5-7 needs)

## Channel Preferences

**Where They Research Solutions**:
| Channel | Role in Decision | Content Expectation |
|---------|-----------------|---------------------|
| [Channel] | [How they use it] | [What they want] |

**Third-Party Sources They Consult**:
- [Source type]: Role in their research
(list review sites, analyst reports, forums, etc.)

## Content Strategy

### Content Themes
| Theme | Why It Resonates | Angle |
|-------|------------------|-------|
| "[Theme]" | Connection to evaluation needs | Approach |
(list 5-7 themes)

### Content Formats for Consideration
| Format | Effectiveness | Purpose | Gate? |
|--------|--------------|---------|-------|
| Comparison Guides | High | Solution education | Yes |
| Buyer's Checklists | High | Evaluation framework | Yes |
| Webinars | Medium-High | Deep education | Yes |
| ROI Frameworks | High | Building internal case | Yes |
(list 7-10 formats)

### Content Ideas - Detailed

**Lead Magnets (Gated)**:
1. **"[Guide/Report Title]"**
   - Value Proposition: What they get
   - Sections: [Outline]
   - Length: [Pages/time]
   - Gate Justification: Why they'd give email

2. **"[Checklist/Template Title]"**
   - Use Case: How they'd use it
   - Format: [Checklist/Spreadsheet/Template]
(provide 5-7 gated content ideas)

**Comparison Content (Ungated)**:
1. **"[Comparison Title]"**
   - Comparison Type: Feature/Approach/Use case
   - Key Differentiators: What to highlight
   - Our Position: Where we fit
(provide 3-5 comparison ideas)

**Educational Webinars**:
1. **"[Webinar Title]"**
   - Learning Objective: What they walk away knowing
   - Format: [Presentation/Demo/Panel]
   - Soft CTA: [Next step]
(provide 2-3 webinar ideas)

## Paid Advertising Strategy

### Campaign Objective
[Consideration / Lead Generation]

### Platform Adjustments
| Platform | Budget Shift | Focus Change |
|----------|-------------|--------------|
| [Platform] | +/-X% | [New focus] |

### Targeting Approach
**Retargeting Pools**:
- Awareness content engagers → [Message]
- Website visitors (specific pages) → [Message]
- Quiz/assessment completers → [Message]

**Intent-Based Targeting**:
- [Signal]: How to target, message
(list 3-5 intent signals)

### Ad Creative Directions

**Angle 1: Education Offer**
- Headline: "The Complete Guide to [Solution Category]"
- Offer: [Lead magnet]
- CTA: Download/Get Access

**Angle 2: Framework/Tool Offer**
- Headline: "[Evaluation Tool] for [Role/Company Type]"
- Offer: [Checklist/Calculator]
- CTA: Get Your [Tool]

**Angle 3: Webinar/Event**
- Headline: "[Educational Topic] - Live Session"
- Offer: Webinar registration
- CTA: Save Your Spot

**Angle 4: Case Study Teaser**
- Headline: "How [Similar Company] [Achieved Result]"
- Offer: Full case study
- CTA: Read the Story

## Success Metrics

| KPI | Target | Measurement |
|-----|--------|-------------|
| Lead magnet downloads | X/month | [Method] |
| Webinar registrations | X/month | [Method] |
| Content engagement depth | X minutes | [Method] |
| Lead quality score | X% SQLs | [Method] |

**Stage Completion Signal**: [Requests demo, pricing, or direct product information]

---

# STAGE 3: DECISION

## Stage Context

**Objective**: Convert prospect from "Product Aware" to "Customer" (purchase)

**Where They Are**:
- Has shortlisted vendors (2-4 typically)
- Actively comparing specific options
- Building business case / seeking approval
- Risk assessment mode

**Key Difference from Consideration**:
- Now comparing *vendors*, not solution types
- Looking for proof and risk reduction
- May involve additional stakeholders
- Price/value conversations happening

**Who Else Is Involved** (B2B):
| Stakeholder | Role | Primary Concern | Content Need |
|-------------|------|-----------------|--------------|
| [Title] | Economic Buyer | [Concern] | [Content type] |
| [Title] | Technical Buyer | [Concern] | [Content type] |
| [Title] | End User | [Concern] | [Content type] |
| [Title] | Champion | [Concern] | [Content type] |

## Questions They're Asking

**Comparison Questions**:
- "How does [your product] compare to [competitor]?"
- "What makes you different from [alternative]?"
- "Is [your product] better for [my specific situation]?"
(list 5-7 comparison questions)

**Proof Questions**:
- "Has this worked for companies like mine?"
- "What results can I realistically expect?"
- "Can I talk to a customer reference?"
(list 5-7 proof questions)

**Risk Questions**:
- "What happens if it doesn't work?"
- "What's your guarantee/refund policy?"
- "How hard is implementation?"
- "What support do I get?"
(list 5-7 risk questions)

**Practical Questions**:
- "What's the total cost of ownership?"
- "How long until I see results?"
- "What resources do we need to commit?"
(list 5-7 practical questions)

## Information Needs

1. **Direct Comparison**: How you stack up vs specific competitors
2. **Proof of Results**: Evidence from similar customers
3. **Risk Mitigation**: Guarantees, support, implementation help
4. **Total Cost Clarity**: All costs, not just sticker price
5. **Implementation Reality**: Honest view of effort required
(list all key information needs)

## Content Strategy

### Content Themes
| Theme | Why It Resonates | Angle |
|-------|------------------|-------|
| "Proof over promises" | They're skeptical of marketing | Lead with data |
| "Risk reversal" | Fear of wrong choice | Guarantees, support |
| "Similar to you" | Need relevance | Industry-specific proof |
(list 5-7 themes)

### Content Formats for Decision
| Format | Purpose | Effectiveness |
|--------|---------|--------------|
| Case Studies | Proof of results | Critical |
| ROI Calculators | Financial justification | Very High |
| Comparison Pages | Direct vendor comparison | Very High |
| Product Demos | See it in action | Critical |
| Customer Testimonials | Social proof | High |
| Implementation Guides | Reduce fear | High |
| Security/Compliance Docs | Risk reduction | High (B2B) |

### Content Ideas - Detailed

**Case Studies**:
Criteria for this ICP - prioritize case studies featuring:
- Industry: [Matching industries]
- Company Size: [Matching size]
- Challenge: [Matching their top pain points]
- Results: [Metrics they care about]

Case Study Structure:
1. **"[Customer Name]: [Compelling Result]"**
   - Challenge: [Their situation before]
   - Solution: [How they used your product]
   - Results: [Specific metrics]
   - Quote: [Powerful testimonial]

**Comparison Content**:
1. **"[Your Product] vs. [Competitor]: Honest Comparison"**
   - Approach: Fair, acknowledge competitor strengths
   - Differentiation: [Key differentiators for this ICP]
   - Best For: [When to choose you vs them]
(provide for top 3-5 competitors)

**Interactive Tools**:
1. **"ROI Calculator: [Use Case Specific]"**
   - Inputs: [What user enters - specific to this ICP]
   - Outputs: [What they see - metrics they care about]
   - Assumptions: [Transparent methodology]
   - CTA: [Talk to sales, start trial]

**Sales Enablement Content**:
1. **"Implementation Guide: What to Expect"**
   - Timeline: Realistic expectations
   - Resources Needed: Honest requirements  
   - Milestones: What success looks like
   - Support: What help they get

## Paid Advertising Strategy

### Campaign Objective
[Conversions / Demo Requests / Trial Signups]

### Retargeting Focus
| Audience Segment | Message Focus | Offer |
|------------------|---------------|-------|
| Visited pricing page | Objection handling | Demo/consultation |
| Downloaded decision-stage content | Urgency/proof | Limited offer |
| Visited comparison pages | Differentiation | Head-to-head demo |
| Engaged with competitor content | Competitive advantage | Switch story |

### Ad Creative Directions

**Angle 1: Proof/Results**
- Headline: "[Customer] achieved [specific result]"
- Body: Tease the case study
- CTA: See how they did it
- Landing: Full case study

**Angle 2: Direct Comparison**
- Headline: "Switching from [Competitor]?"
- Body: Key differentiators
- CTA: See the comparison
- Landing: Comparison page

**Angle 3: Risk Reversal**
- Headline: "[Guarantee/Trial offer]"
- Body: Reduce perceived risk
- CTA: Try risk-free
- Landing: Trial signup

**Angle 4: Urgency/Scarcity** (if appropriate)
- Headline: "[Time-limited offer]"
- Body: Reason for urgency
- CTA: Claim offer
- Landing: Special offer page

**Angle 5: Objection Handling**
- Headline: "Worried about [common objection]?"
- Body: Address concern directly
- CTA: Learn how we handle [objection]
- Landing: FAQ/objection page

## Success Metrics

| KPI | Target | Measurement |
|-----|--------|-------------|
| Demo requests | X/month | [Method] |
| Trial signups | X/month | [Method] |
| Proposal requests | X/month | [Method] |
| Win rate | X% | [Method] |
| Sales cycle length | X days | [Method] |

**Stage Completion Signal**: [Signed contract / completed purchase / started paid plan]

---

# STAGE 4: ONBOARDING

## Stage Context

**Objective**: Minimize Time-to-Value (TTV), ensure successful activation, prevent early churn

**Where They Are**:
- Just purchased, excitement mixed with anxiety
- "Post-purchase rationalization" period
- Facing implementation reality
- Need quick wins to validate decision

**The Danger Zone**:
- "Trough of Disillusionment" risk
- Buyer's remorse possibility
- Complexity overwhelm
- Day 1-30 churn risk highest

**Critical Success Factors**:
- Time to first value (how fast they see results)
- Feature adoption (using core features)
- Support responsiveness (when stuck)
- Progress visibility (knowing they're on track)

## Success Milestones

| Milestone | Target Timeline | Why Critical | How to Ensure |
|-----------|-----------------|--------------|---------------|
| Account setup complete | Day 1 | Momentum, commitment | Automated, simple |
| First "[quick win action]" | Day 1-3 | Value validation | Guided experience |
| Core feature #1 used | Week 1 | Habit formation | Prompts, checklist |
| Core feature #2 used | Week 1-2 | Deeper value | Educational content |
| "[Value milestone]" achieved | Week 2-4 | ROI demonstrated | Success tracking |

**Quick Win Opportunities** (first 48 hours):
1. [Win]: How to guide them there
2. [Win]: How to guide them there
3. [Win]: How to guide them there
(wins should be achievable with minimal effort but demonstrate clear value)

## Customer Questions

**Immediate Questions** (Day 1):
- "What do I do first?"
- "How do I get set up?"
- "Where do I find [basic feature]?"

**Week 1 Questions**:
- "Am I doing this right?"
- "What should I focus on?"
- "How do I [accomplish first goal]?"

**Week 2-4 Questions**:
- "How do I get better results?"
- "What am I missing?"
- "How do others use this?"

## Content Strategy

### Onboarding Content Sequence

| Day | Content | Delivery | Goal |
|-----|---------|----------|------|
| 0 | Welcome email + quick start | Email | Set expectations |
| 1 | First action prompt | Email + In-app | Complete setup |
| 2 | Quick win tutorial | Email + In-app | First success |
| 3 | Feature highlight | Email | Expand usage |
| 5 | Progress check + tips | Email | Validate progress |
| 7 | Success milestone | Email | Celebrate |
| 14 | Advanced feature intro | Email | Deepen engagement |
| 21 | Results check + help offer | Email | Ensure satisfaction |
| 30 | Success review | Email | Confirm value |

### Content Formats for Onboarding

| Format | Purpose | Delivery | Priority |
|--------|---------|----------|----------|
| Welcome Video | Set expectations, humanize | Email | High |
| Setup Checklist | Clear path forward | In-app | Critical |
| Quick Start Guide | Get first win | In-app + Help docs | Critical |
| Feature Tutorials | Learn specific features | In-app tooltips | High |
| Template Library | Remove blank page syndrome | In-app | High |
| Progress Tracker | Show advancement | In-app | Medium |
| FAQ/Troubleshooting | Self-service support | Help docs | High |
| Office Hours/Live Help | Human assistance | Calendar | Medium |

### Content Ideas - Detailed

**Welcome Sequence**:
1. **Welcome Email: "You're In - Here's Your First Step"**
   - Tone: Excited but focused
   - Key Message: One clear action
   - CTA: [Specific first action]

2. **Email Day 1: "Complete Your Setup in 5 Minutes"**
   - Content: Setup checklist
   - Value: Get to first win faster
   - CTA: [Complete setup]

3. **Email Day 2: "[First Quick Win] in 2 Minutes"**
   - Content: Tutorial for quick win
   - Value: Immediate value demonstration
   - CTA: [Do the thing]

(continue for full 30-day sequence)

**Quick Start Guides**:
1. **"Get [First Result] in Under 10 Minutes"**
   - Format: Step-by-step with screenshots/video
   - Assumption: Complete beginner
   - End State: Tangible result

**Templates/Presets**:
1. **"[Use Case] Template Pack"**
   - Contents: Pre-built examples for their use case
   - Value: Skip the blank page
   - Customization: What to personalize

## Re-engagement Triggers

| Risk Signal | Automated Response | Human Escalation |
|-------------|-------------------|------------------|
| No login Day 3+ | Email: "Need help?" | Flag for CS if Day 7+ |
| Setup incomplete Day 5+ | Email: "Your quick start checklist" | CS reach out Day 7+ |
| Core feature unused Week 1 | In-app prompt + email tutorial | CS check-in |
| Support ticket without resolution | Escalation email | Immediate CS follow-up |
| Low engagement score | Re-engagement campaign | CS call |

## Success Metrics

| KPI | Target | Measurement |
|-----|--------|-------------|
| Activation rate | X% complete [milestone] by Day X | [Definition] |
| Time to first value | X days average | [Measurement] |
| Feature adoption | X% using [core features] by Week 2 | [Which features] |
| Support tickets | <X per user | [Normal vs concerning] |
| Day 30 retention | X% still active | [Active definition] |
| CSAT/Onboarding NPS | X+ | [Survey timing] |

**Stage Completion Signal**: [Active user threshold - specific definition]

---

# STAGE 5: EXPANSION

## Stage Context

**Objective**: Maximize Customer Lifetime Value through retention, expansion, and advocacy

**Where They Are**:
- Actively using product, seeing value
- Trust established
- Open to deeper relationship
- Potential to expand or advocate

**Expansion Opportunities**:
1. **Retention**: Keep them (prevent churn)
2. **Upsell**: Higher tier, more features
3. **Cross-sell**: Additional products
4. **Expansion**: More seats, more usage
5. **Advocacy**: Referrals, reviews, case studies

## Expansion Triggers

### Usage-Based Triggers
| Trigger Behavior | Opportunity | Approach |
|------------------|-------------|----------|
| Hitting usage limits (80%+) | Upgrade tier | Proactive offer + value justification |
| Using feature heavily | Power user path | Advanced training + advocacy ask |
| New use case emerging | Cross-sell | Educational content + soft pitch |
| Added team members | Expansion | Team training + additional seats |
| Achieved success milestone | Advocacy | Review/referral/case study ask |

### Time-Based Triggers
| Milestone | Opportunity | Approach |
|-----------|-------------|----------|
| 30-day anniversary | Advocacy (if healthy) | Review request |
| Renewal approaching | Retention + upgrade | Value review + new features |
| Quarter/Year milestone | Case study | Success story capture |
| After major success | Referral | Referral program intro |

### Health Indicators
| Indicator | Weight | Healthy | At-Risk |
|-----------|--------|---------|---------|
| Login frequency | X% | [Threshold] | [Threshold] |
| Feature adoption | X% | [Threshold] | [Threshold] |
| Support sentiment | X% | [Threshold] | [Threshold] |
| Engagement trend | X% | [Threshold] | [Threshold] |

## Content Strategy

### Content Themes for Expansion
| Theme | Goal | Approach |
|-------|------|----------|
| "Advanced mastery" | Deepen engagement | Power user content |
| "What's new" | Showcase value/investment | Product updates |
| "Insider access" | Build loyalty | Early access, roadmap |
| "Community belonging" | Stickiness | User community |
| "Success recognition" | Ego, advocacy | User spotlights |

### Content Formats for Expansion
| Format | Purpose | Trigger | Expected Outcome |
|--------|---------|---------|------------------|
| Advanced tutorials | Deeper feature adoption | Feature underuse | Increased usage |
| New feature announcements | Show ongoing value | Release schedule | Feature adoption |
| Best practices webinars | Optimization | Quarterly | Engagement |
| Customer community | Peer learning, stickiness | Onboarding | Retention |
| Success spotlights | Recognition, proof | Success milestone | Advocacy |
| Insider newsletter | Exclusivity, roadmap | Monthly | Loyalty |
| Year-in-review | Value summary | Annual | Retention |

### Content Ideas - Detailed

**Power User Content**:
1. **"Advanced [Feature] Techniques: 10 Tips from Power Users"**
   - Format: Long-form guide or webinar
   - Audience: Active users ready to level up
   - Hidden CTA: Shows value of higher tier

2. **"Workflow: How [Power User] Uses [Product] for [Advanced Use Case]"**
   - Format: Case study / video
   - Value: Learn from peers
   - Advocacy: Features the customer

**Community Building**:
1. **Monthly "Office Hours" / AMA**
   - Format: Live session with product team
   - Value: Access to experts
   - Benefit: Feedback loop, engagement

2. **User Community / Slack / Forum**
   - Format: Peer community
   - Value: Peer support, tips sharing
   - Benefit: Stickiness, reduced support load

**Advocacy Recruitment**:
1. **"[Product] Champions" Program**
   - Benefits: Early access, recognition, rewards
   - Ask: Reviews, referrals, case studies
   - Structure: Tiered with increasing benefits

## Expansion Campaigns

### Upsell Campaigns
**Trigger**: [Usage threshold / Feature request / Time]
**Message Framework**:
- Acknowledge current success
- Highlight limitation they're hitting
- Show value of upgrade
- Make transition easy

**Example Email Sequence**:
1. "You're getting great results - here's how to 10x them"
2. "You've hit [limit] - here's what [next tier] unlocks"
3. "[Special upgrade offer]"

### Referral Program
**Incentive Structure**:
- Referrer gets: [Incentive]
- Referee gets: [Incentive]
- Timing: When to ask (after success milestone)

**Referral Content**:
1. **Referral Program Announcement Email**
2. **Share Template (easy for them to use)**
3. **Thank You + Reward Delivery**

### Review/Testimonial Collection
**Timing**: After positive NPS score or success milestone

**Ask Sequence**:
1. **NPS Survey** (identify promoters)
2. **Review Request Email** (if 9-10 NPS)
3. **Case Study Recruitment** (if exceptional results)

**Platforms for Reviews**:
- [Platform 1]: Why important for this ICP
- [Platform 2]: Why important
(list review sites relevant to this ICP)

## Retention Tactics

### At-Risk Interventions
| Risk Signal | Intervention | Owner | Timeline |
|-------------|--------------|-------|----------|
| Declining usage | [Specific action] | CS | [Timing] |
| Support issues | [Specific action] | CS | [Timing] |
| Feature disuse | [Specific action] | Marketing | [Timing] |
| Negative feedback | [Specific action] | CS | [Timing] |

### Proactive Retention
| Activity | Frequency | Goal |
|----------|-----------|------|
| Quarterly business review | Quarterly | Value reinforcement |
| Usage report/insights | Monthly | Demonstrate value |
| Roadmap preview | As available | Show investment |
| Success check-in | [Trigger-based] | Early warning |

## Success Metrics

| KPI | Target | Measurement |
|-----|--------|-------------|
| Net Revenue Retention | X%+ | Annual |
| Gross Revenue Retention | X%+ | Annual |
| Expansion Revenue % | X% of total | Monthly |
| Customer LTV | $X | Cohort analysis |
| NPS | X+ | Quarterly |
| Referral rate | X% | Monthly |
| Review count/rating | X reviews, X.X stars | [Platform] |
| Churn rate | <X% | Monthly |

---

# JOURNEY SUMMARY

## Overall Journey Timeline

| Stage | Typical Duration | Primary Owner | Exit Criteria |
|-------|------------------|---------------|---------------|
| Awareness | [Duration] | Marketing | Downloads consideration content |
| Consideration | [Duration] | Marketing | Requests demo/pricing |
| Decision | [Duration] | Sales + Marketing | Purchases |
| Onboarding | [Duration] | Customer Success | Reaches activation milestone |
| Expansion | Ongoing | CS + Marketing | Continuous value delivery |

## Key Decision Points

The 5 critical moments where the prospect could be won or lost:

| # | Decision Point | Stage | Stakes | How to Win |
|---|----------------|-------|--------|------------|
| 1 | First content interaction | Awareness | Captures attention or lost forever | Strong hook, immediate value |
| 2 | Lead magnet exchange | Consideration | Email for value | High-value content |
| 3 | Vendor shortlisting | Decision | Makes the cut or doesn't | Clear differentiation |
| 4 | First week experience | Onboarding | Sticks or churns | Fast time-to-value |
| 5 | Renewal decision | Expansion | Long-term relationship | Demonstrated ROI |

## Recommended Touchpoint Sequence

Optimal path through the journey:

| # | Stage | Channel | Content/Action | Purpose | Trigger |
|---|-------|---------|----------------|---------|---------|
| 1 | Awareness | Social Ad | Pain validation video | Initial capture | Interest targeting |
| 2 | Awareness | Blog | Problem education article | Deeper engagement | Ad click |
| 3 | Awareness | Quiz | Self-assessment | Lead capture | Content engagement |
| 4 | Consideration | Email | Lead magnet delivery | Education | Quiz completion |
| 5 | Consideration | Webinar | Solution education | Build trust | Lead magnet download |
| 6 | Consideration | Email | Case study | Proof | Webinar attendance |
| 7 | Decision | Retargeting Ad | Demo offer | Conversion | Website activity |
| 8 | Decision | Demo | Live product walkthrough | Close | Demo request |
| 9 | Decision | Email | Proposal + social proof | Urgency | Post-demo |
| 10 | Onboarding | Email | Welcome + first action | Activation | Purchase |
| 11 | Onboarding | In-app | Quick win tutorial | Early success | First login |
| 12 | Onboarding | Email | Feature education | Adoption | Day 3 |
| 13 | Onboarding | Email | Success check-in | Support | Day 7 |
| 14 | Expansion | Email | Advanced tips | Deepen usage | Day 30 |
| 15 | Expansion | Email | Referral ask | Advocacy | Positive NPS |

(Customize for specific ICP)

## Content Map by Stage

| Stage | Content | Format | Goal | Owner |
|-------|---------|--------|------|-------|
| Awareness | [List top 3-5] | | | |
| Consideration | [List top 3-5] | | | |
| Decision | [List top 3-5] | | | |
| Onboarding | [List top 3-5] | | | |
| Expansion | [List top 3-5] | | | |

---

Provide this complete journey map analysis for the specified ICP.
```

---

## Output Format

The journey map should be output as human-readable Markdown (not JSON) suitable for:
1. Direct use by marketing team members
2. Export to DOCX for marketing strategy documents
3. Easy scanning and reference during campaign planning

Use:
- Clear headers and subheaders
- Tables for structured comparisons
- Bullet points for lists
- Bold for emphasis on key terms
- Specific, actionable content ideas (not generic placeholder text)