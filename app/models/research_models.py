"""
Cognitive Resonance Engine - Data Models
========================================
Pydantic models for all research data structures.
"""

from typing import List, Dict, Optional, Any
from pydantic import BaseModel, Field
from datetime import datetime
from enum import Enum


# ===== Enums =====

class BusinessModelType(str, Enum):
    B2B = "B2B"
    B2C = "B2C"
    BOTH = "Both"


class DecisionStyle(str, Enum):
    ANALYTICAL = "Analytical"
    INTUITIVE = "Intuitive"
    CONSENSUS = "Consensus"
    COLLABORATIVE = "Collaborative"
    DECISIVE = "Decisive"
    DELEGATOR = "Delegator"


class RiskTolerance(str, Enum):
    RISK_AVERSE = "Risk-Averse"
    MODERATE = "Moderate"
    RISK_SEEKING = "Risk-Seeking"


class PainSeverity(str, Enum):
    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"
    CRITICAL = "Critical"


# ===== Input Models =====

class ClientInput(BaseModel):
    """User input for client information."""
    client_name: str = Field(..., description="Company/Brand name")
    website_url: str = Field(..., description="Main website URL")
    about_page_url: Optional[str] = Field(None, description="About Us page URL")
    products_services_url: Optional[str] = Field(
        None, description="Products/Services page URL"
    )
    additional_urls: List[str] = Field(
        default_factory=list, description="Additional relevant URLs"
    )
    industry: str = Field(..., description="Industry category")
    business_model: BusinessModelType = Field(
        ..., description="B2B, B2C, or Both"
    )
    target_market: Optional[str] = Field(
        None, description="Geographic/demographic focus"
    )
    known_competitors: Optional[str] = Field(
        None, description="Known competitor names"
    )
    additional_context: Optional[str] = Field(
        None, description="Any additional context"
    )
    num_icps: int = Field(default=3, ge=2, le=5, description="Number of ICPs")


# ===== Company Profile Models =====

class Competitor(BaseModel):
    """Competitor information."""
    name: str
    website: Optional[str] = None
    description: Optional[str] = None
    key_differentiators: List[str] = Field(default_factory=list)
    strengths: List[str] = Field(default_factory=list)
    weaknesses: List[str] = Field(default_factory=list)
    target_audience: Optional[str] = None
    market_position: Optional[str] = None


class ProductService(BaseModel):
    """Product or service offering."""
    name: str
    description: str
    features: List[str] = Field(default_factory=list)
    target_user: Optional[str] = None
    target_audience: Optional[str] = None
    pricing_tier: Optional[str] = None
    unique_aspects: List[str] = Field(default_factory=list)


class BrandVoice(BaseModel):
    """Brand voice characteristics."""
    tone: str = Field(default="", description="e.g., Professional, Friendly, Technical")
    complexity_level: Optional[str] = Field(None, description="Simple, Moderate, Technical")
    themes: List[str] = Field(default_factory=list)
    key_themes: List[str] = Field(default_factory=list)
    taglines: List[str] = Field(default_factory=list)
    emotional_appeals: List[str] = Field(default_factory=list)


class CompanyProfile(BaseModel):
    """Complete company profile from research."""
    name: str
    website_url: str
    industry: str
    business_model: BusinessModelType
    overview: str = ""
    products_services: List[ProductService] = Field(default_factory=list)
    stated_value_propositions: List[str] = Field(default_factory=list)
    stated_target_audience: Optional[str] = None
    brand_voice: Optional[Any] = None  # Can be BrandVoice or dict
    competitors: List[Competitor] = Field(default_factory=list)
    trust_signals: List[str] = Field(default_factory=list)
    content_themes: List[str] = Field(default_factory=list)
    market_gaps: List[str] = Field(default_factory=list)
    market_trends: List[str] = Field(default_factory=list)
    founding_story: Optional[str] = None
    mission_statement: Optional[str] = None
    vision_statement: Optional[str] = None
    core_values: List[str] = Field(default_factory=list)
    raw_research: Optional[str] = None


# ===== ICP Models =====

class Demographics(BaseModel):
    """Demographics/Firmographics."""
    # B2B fields
    company_size: Optional[str] = None
    annual_revenue: Optional[str] = None
    industry_verticals: List[str] = Field(default_factory=list)
    company_stage: Optional[str] = None
    department: Optional[str] = None
    job_titles: List[str] = Field(default_factory=list)
    seniority_level: Optional[str] = None
    budget_range: Optional[str] = None
    
    # B2C fields
    age_range: Optional[str] = None
    gender_skew: Optional[str] = None
    income_bracket: Optional[str] = None
    income_range: Optional[str] = None
    education_level: Optional[str] = None
    family_status: Optional[str] = None
    location_type: Optional[str] = None
    
    # Common
    geographic_focus: Optional[str] = None


class Psychographics(BaseModel):
    """Psychographic profile."""
    core_values: List[str] = Field(default_factory=list)
    aspirations: List[str] = Field(default_factory=list)
    decision_style: DecisionStyle = DecisionStyle.ANALYTICAL
    risk_tolerance: RiskTolerance = RiskTolerance.MODERATE
    personality_indicators: Dict[str, str] = Field(default_factory=dict)
    personality_traits: List[str] = Field(default_factory=list)
    lifestyle_priorities: List[str] = Field(default_factory=list)
    fears: List[str] = Field(default_factory=list)
    status_concerns: List[str] = Field(default_factory=list)


class BehavioralProfile(BaseModel):
    """Behavioral characteristics."""
    buying_process: Optional[str] = None
    research_channels: List[str] = Field(default_factory=list)
    decision_timeline: Optional[str] = None
    decision_influencers: List[str] = Field(default_factory=list)
    key_influencers: List[str] = Field(default_factory=list)
    preferred_content_formats: List[str] = Field(default_factory=list)
    content_preferences: List[str] = Field(default_factory=list)
    engagement_patterns: Optional[str] = None
    technology_adoption: Optional[str] = None
    current_solutions: List[str] = Field(default_factory=list)
    purchase_triggers: List[str] = Field(default_factory=list)
    objections: List[str] = Field(default_factory=list)


class Motivation(BaseModel):
    """Customer motivation."""
    statement: str
    type: Optional[str] = Field(None, description="Internal or External")
    category: str = "functional"
    intensity: int = Field(default=5, ge=1, le=10)
    trigger_event: Optional[str] = None


class PainPoint(BaseModel):
    """Customer pain point."""
    statement: str
    category: str = "functional"
    severity: int = Field(default=5, ge=1, le=10)
    frequency: Optional[str] = None
    current_workaround: Optional[str] = None
    current_coping: Optional[str] = None
    content_strategy: Optional[str] = None


class Goal(BaseModel):
    """Customer goal."""
    statement: str
    timeframe: str = Field(default="", description="Immediate or Long-term")
    success_metric: Optional[str] = None


class Fear(BaseModel):
    """Customer fear."""
    statement: str
    underlying_anxiety: Optional[str] = None
    trigger_situations: List[str] = Field(default_factory=list)


class IdealCustomerProfile(BaseModel):
    """Complete Ideal Customer Profile."""
    icp_id: Optional[str] = None
    icp_name: str
    one_liner: str = ""
    segment_priority: str = Field(default="medium", description="Primary, Secondary, Niche, high, medium, low")
    
    demographics: Demographics = Field(default_factory=Demographics)
    psychographics: Psychographics = Field(default_factory=Psychographics)
    behavioral: BehavioralProfile = Field(default_factory=BehavioralProfile)
    
    motivations: List[Motivation] = Field(default_factory=list)
    pain_points: List[PainPoint] = Field(default_factory=list)
    goals: List[Goal] = Field(default_factory=list)
    fears: List[Fear] = Field(default_factory=list)
    
    detailed_narrative: Optional[str] = None
    messaging_hooks: List[str] = Field(default_factory=list)


# Alias for convenience
ICP = IdealCustomerProfile


# ===== Value Proposition Models =====

class CustomerJob(BaseModel):
    """Customer job to be done."""
    statement: str
    job_type: str = Field(default="", description="Functional, Social, or Emotional")
    importance: str = Field(default="", description="Critical, Important, Nice-to-have")
    frequency: Optional[str] = None


class Pain(BaseModel):
    """Customer pain from VPC."""
    statement: str
    severity: int = Field(default=5, ge=1, le=10)
    pain_type: str = Field(default="", description="Functional, Financial, Emotional")


class Gain(BaseModel):
    """Customer gain from VPC."""
    statement: str
    gain_type: str = Field(default="", description="Required, Expected, Desired, Unexpected")
    importance: str = ""


class PainReliever(BaseModel):
    """How product relieves pain."""
    pain_addressed: str
    how_relieved: str
    feature_or_capability: str = ""
    strength: str = Field(default="", description="Strong, Moderate, Weak")
    relief_significance: int = Field(default=5, ge=1, le=10)
    evidence: Optional[str] = None


class GainCreator(BaseModel):
    """How product creates gain."""
    gain_created: str
    how_created: str
    feature_or_capability: str = ""
    strength: str = ""
    creation_significance: int = Field(default=5, ge=1, le=10)
    evidence: Optional[str] = None


class ValuePropositionCanvas(BaseModel):
    """Complete Value Proposition Canvas."""
    icp_id: Optional[str] = None
    icp_name: Optional[str] = None
    
    # Customer Profile side
    customer_jobs: Any = Field(default_factory=dict)  # Can be dict or list
    pains: List[Pain] = Field(default_factory=list)
    gains: List[Gain] = Field(default_factory=list)
    customer_pains: List[Any] = Field(default_factory=list)
    customer_gains: List[Any] = Field(default_factory=list)
    
    # Value Map side
    products_services: List[str] = Field(default_factory=list)
    products_services_fit: List[Any] = Field(default_factory=list)
    pain_relievers: List[PainReliever] = Field(default_factory=list)
    gain_creators: List[GainCreator] = Field(default_factory=list)
    
    # Fit analysis
    fit_score: Optional[float] = Field(None, ge=0, le=100)
    fit_analysis: Optional[str] = None
    unique_differentiators: List[str] = Field(default_factory=list)
    commodity_features: List[str] = Field(default_factory=list)
    gaps_weaknesses: List[str] = Field(default_factory=list)
    messaging_recommendations: List[str] = Field(default_factory=list)
    
    # Value proposition statement
    value_proposition_statement: Optional[str] = None


# ===== Pain Point Taxonomy Models =====

class DetailedPainPoint(BaseModel):
    """Detailed pain point with full context."""
    statement: str
    category: str = "functional"
    severity: int = Field(default=5, ge=1, le=10)
    frequency: Optional[str] = None
    current_coping_mechanism: Optional[str] = None
    impact_if_unresolved: Optional[str] = None
    root_cause: Optional[str] = None
    five_whys_depth: Optional[str] = None
    estimated_cost_impact: Optional[str] = None
    trigger_situations: List[str] = Field(default_factory=list)
    underlying_fear: Optional[str] = None
    time_impact: Optional[str] = None
    current_workaround: Optional[str] = None
    content_strategy: Optional[str] = None


class FunctionalPain(BaseModel):
    """Functional pain point."""
    statement: str
    category: str = "inefficiency"  # Inefficiency, Complexity, Inaccuracy, etc.
    severity: int = Field(default=5, ge=1, le=10)
    frequency: Optional[str] = None
    time_impact: Optional[str] = None
    current_workaround: Optional[str] = None
    current_coping_mechanism: Optional[str] = None
    impact_if_unresolved: Optional[str] = None
    root_cause: Optional[str] = None
    five_whys_depth: Optional[str] = None
    content_strategy: Optional[str] = None


class FinancialPain(BaseModel):
    """Financial pain point."""
    statement: str
    category: str = "direct_cost"  # Direct Cost, Hidden Costs, ROI Uncertainty, etc.
    severity: int = Field(default=5, ge=1, le=10)
    frequency: Optional[str] = None
    impact: Optional[str] = None
    estimated_cost_impact: Optional[str] = None
    current_coping_mechanism: Optional[str] = None
    impact_if_unresolved: Optional[str] = None
    root_cause: Optional[str] = None
    content_strategy: Optional[str] = None


class EmotionalPain(BaseModel):
    """Emotional pain point."""
    statement: str
    category: str = "anxiety"  # Anxiety, Frustration, Overwhelm, etc.
    severity: int = Field(default=5, ge=1, le=10)
    frequency: Optional[str] = None
    underlying_fear: Optional[str] = None
    trigger_situations: List[str] = Field(default_factory=list)
    current_coping_mechanism: Optional[str] = None
    impact_if_unresolved: Optional[str] = None
    content_strategy: Optional[str] = None


class ForcesOfProgressAnalysis(BaseModel):
    """Four Forces of Progress analysis."""
    push_factors: List[str] = Field(default_factory=list)
    pull_factors: List[str] = Field(default_factory=list)
    habit_factors: List[str] = Field(default_factory=list)
    anxiety_factors: List[str] = Field(default_factory=list)
    net_force_assessment: Optional[str] = None
    recommended_focus: Optional[str] = None
    key_trigger_moments: List[str] = Field(default_factory=list)


# Alias for compatibility
ForcesAnalysis = ForcesOfProgressAnalysis


class FiveWhysAnalysis(BaseModel):
    """Five Whys root cause analysis."""
    surface_pain: str
    why_1: str
    why_2: str
    why_3: str
    why_4: str
    root_cause: str
    marketing_implication: Optional[str] = None


class PainPointTaxonomy(BaseModel):
    """Complete pain point taxonomy."""
    icp_id: Optional[str] = None
    icp_name: Optional[str] = None
    
    functional_pains: List[Any] = Field(default_factory=list)
    financial_pains: List[Any] = Field(default_factory=list)
    emotional_pains: List[Any] = Field(default_factory=list)
    
    forces_analysis: Optional[ForcesOfProgressAnalysis] = None
    five_whys_analyses: List[FiveWhysAnalysis] = Field(default_factory=list)
    
    switching_barriers: List[str] = Field(default_factory=list)
    switching_triggers: List[str] = Field(default_factory=list)
    pain_priority_ranking: List[Any] = Field(default_factory=list)
    messaging_implications: List[str] = Field(default_factory=list)


# ===== Journey Map Models =====

class ContentIdea(BaseModel):
    """Content idea for a journey stage."""
    title: str
    format: str = "blog"
    hook: Optional[str] = None
    key_points: List[str] = Field(default_factory=list)
    key_message: Optional[str] = None
    cta: Optional[str] = None


class AdCreative(BaseModel):
    """Ad creative direction."""
    angle: str
    headline: str
    body_direction: Optional[str] = None
    emotional_trigger: Optional[str] = None
    cta: Optional[str] = None


class JourneyStage(BaseModel):
    """Single journey stage."""
    stage_id: Optional[str] = None
    stage_name: Optional[str] = None
    
    # Customer context
    objective: str = ""
    customer_mindset: Optional[str] = None
    knowledge_level: Optional[str] = None
    emotional_state: List[str] = Field(default_factory=list)
    
    # Questions and needs
    key_questions: List[str] = Field(default_factory=list)
    information_needs: List[str] = Field(default_factory=list)
    
    # Channels
    preferred_channels: List[str] = Field(default_factory=list)
    
    # Content strategy
    content_themes: List[str] = Field(default_factory=list)
    content_formats: List[str] = Field(default_factory=list)
    content_ideas: List[ContentIdea] = Field(default_factory=list)
    
    # Campaign recommendations
    ad_campaign_angle: Optional[str] = None
    ad_creatives: List[AdCreative] = Field(default_factory=list)
    targeting_approach: Optional[str] = None
    targeting_criteria: List[str] = Field(default_factory=list)
    
    # Metrics
    kpis: List[str] = Field(default_factory=list)
    stage_completion_signal: Optional[str] = None


class Touchpoint(BaseModel):
    """Customer touchpoint."""
    sequence: int
    stage: str
    channel: str
    content_type: str
    purpose: str
    trigger: Optional[str] = None


class CustomerJourneyMap(BaseModel):
    """Complete customer journey map."""
    icp_id: Optional[str] = None
    icp_name: Optional[str] = None
    
    # 5 stages
    awareness_stage: Optional[JourneyStage] = None
    consideration_stage: Optional[JourneyStage] = None
    decision_stage: Optional[JourneyStage] = None
    onboarding_stage: Optional[JourneyStage] = None
    expansion_stage: Optional[JourneyStage] = None
    
    # Summary
    overall_timeline: Optional[str] = None
    key_decision_points: List[str] = Field(default_factory=list)
    touchpoint_sequence: List[Touchpoint] = Field(default_factory=list)
    cross_stage_recommendations: List[str] = Field(default_factory=list)
    content_calendar_priorities: List[Any] = Field(default_factory=list)


# ===== Complete Research Results =====

class ICPResearchResult(BaseModel):
    """Complete research results for a single ICP."""
    icp: IdealCustomerProfile
    value_proposition: Optional[ValuePropositionCanvas] = None
    pain_taxonomy: Optional[PainPointTaxonomy] = None
    journey_map: Optional[CustomerJourneyMap] = None


# Alias for compatibility
ICPAnalysisResult = ICPResearchResult


class ResearchResults(BaseModel):
    """Complete research results for a client."""
    client_input: ClientInput
    company_profile: Optional[CompanyProfile] = None
    icps: List[ICPResearchResult] = Field(default_factory=list)
    
    # Raw data storage
    raw_research_data: Dict[str, Any] = Field(default_factory=dict)
    
    # Metadata
    created_at: datetime = Field(default_factory=datetime.now)
    analysis_model: Optional[str] = None
    research_model: Optional[str] = None
    
    # Cost tracking
    total_cost: float = 0.0
    total_tokens: int = 0
    cost_summary: Dict[str, Any] = Field(default_factory=dict)
    
    # Error handling
    error: Optional[str] = None


# ===== Session State Model =====

class SessionState(BaseModel):
    """Session state for Streamlit."""
    client_input: Optional[ClientInput] = None
    results: Optional[ResearchResults] = None
    current_stage: Optional[str] = None
    stage_progress: Dict[str, str] = Field(default_factory=dict)
    error_message: Optional[str] = None
    is_running: bool = False