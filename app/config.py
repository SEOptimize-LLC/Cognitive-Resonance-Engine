"""
Cognitive Resonance Engine - Configuration
==========================================
Central configuration for models, pricing, and application settings.
"""

from typing import Dict, Any
from dataclasses import dataclass
from enum import Enum


# ===== Model Definitions =====

class ModelProvider(str, Enum):
    """Supported model providers via OpenRouter."""
    PERPLEXITY = "perplexity"
    ANTHROPIC = "anthropic"
    GOOGLE = "google"
    OPENAI = "openai"
    XAI = "x-ai"


@dataclass
class ModelConfig:
    """Configuration for a single model."""
    id: str
    name: str
    provider: ModelProvider
    input_price_per_million: float
    output_price_per_million: float
    max_tokens: int
    description: str
    supports_web_search: bool = False


# Available models via OpenRouter
AVAILABLE_MODELS: Dict[str, ModelConfig] = {
    "perplexity/sonar-deep-research": ModelConfig(
        id="perplexity/sonar-deep-research",
        name="Perplexity Sonar Deep Research",
        provider=ModelProvider.PERPLEXITY,
        input_price_per_million=5.00,
        output_price_per_million=5.00,
        max_tokens=8192,
        description="Specialized for web research and information gathering",
        supports_web_search=True
    ),
    "anthropic/claude-sonnet-4.5": ModelConfig(
        id="anthropic/claude-sonnet-4.5",
        name="Claude Sonnet 4.5",
        provider=ModelProvider.ANTHROPIC,
        input_price_per_million=3.00,
        output_price_per_million=15.00,
        max_tokens=8192,
        description="Advanced reasoning and analysis"
    ),
    "google/gemini-2.5-flash-preview-09-2025": ModelConfig(
        id="google/gemini-2.5-flash-preview-09-2025",
        name="Gemini 2.5 Flash Preview",
        provider=ModelProvider.GOOGLE,
        input_price_per_million=0.075,
        output_price_per_million=0.30,
        max_tokens=8192,
        description="Fast and cost-effective"
    ),
    "openai/gpt-5-mini": ModelConfig(
        id="openai/gpt-5-mini",
        name="GPT-5 Mini",
        provider=ModelProvider.OPENAI,
        input_price_per_million=0.15,
        output_price_per_million=0.60,
        max_tokens=16384,
        description="Efficient general-purpose model"
    ),
    "openai/gpt-4.1": ModelConfig(
        id="openai/gpt-4.1",
        name="GPT-4.1",
        provider=ModelProvider.OPENAI,
        input_price_per_million=2.00,
        output_price_per_million=8.00,
        max_tokens=8192,
        description="High-quality reasoning and generation"
    ),
    "x-ai/grok-4.1-fast": ModelConfig(
        id="x-ai/grok-4.1-fast",
        name="Grok 4.1 Fast",
        provider=ModelProvider.XAI,
        input_price_per_million=2.00,
        output_price_per_million=8.00,
        max_tokens=8192,
        description="Fast inference with strong reasoning"
    ),
}

# Models for the dropdown (analysis models - excludes Perplexity which is always used for research)
ANALYSIS_MODELS = {
    k: v for k, v in AVAILABLE_MODELS.items() 
    if not v.supports_web_search
}

# Default models
DEFAULT_RESEARCH_MODEL = "perplexity/sonar-deep-research"
DEFAULT_ANALYSIS_MODEL = "anthropic/claude-sonnet-4.5"

# Aliases for clarity
PERPLEXITY_RESEARCH_MODEL = DEFAULT_RESEARCH_MODEL


# ===== Industry Options =====

INDUSTRIES = [
    "Technology / SaaS",
    "E-commerce / Retail",
    "Healthcare / Medical",
    "Finance / Banking",
    "Education / EdTech",
    "Real Estate",
    "Manufacturing",
    "Professional Services",
    "Marketing / Advertising",
    "Media / Entertainment",
    "Travel / Hospitality",
    "Food & Beverage",
    "Automotive",
    "Energy / Utilities",
    "Non-Profit",
    "Government",
    "Other"
]

BUSINESS_MODELS = [
    "B2B (Business to Business)",
    "B2C (Business to Consumer)",
    "Both B2B and B2C"
]


# ===== Application Settings =====

APP_CONFIG = {
    "app_name": "Cognitive Resonance Engine",
    "app_description": "AI-powered audience research and customer intelligence platform",
    "version": "1.0.0",
    
    # Research settings
    "default_num_icps": 3,
    "min_icps": 2,
    "max_icps": 5,
    
    # API settings
    "openrouter_base_url": "https://openrouter.ai/api/v1",
    "request_timeout": 120,  # seconds
    "max_retries": 3,
    
    # Export settings
    "export_formats": ["markdown", "docx"],
}


# ===== Pipeline Stages =====

PIPELINE_STAGES = [
    {
        "id": "data_ingestion",
        "name": "Data Ingestion",
        "description": "Researching company information",
        "model_type": "research"
    },
    {
        "id": "audience_research",
        "name": "Audience Research",
        "description": "Generating Ideal Customer Profiles",
        "model_type": "analysis"
    },
    {
        "id": "usp_extraction",
        "name": "Value Proposition Analysis",
        "description": "Mapping value propositions to customer needs",
        "model_type": "analysis"
    },
    {
        "id": "pain_taxonomy",
        "name": "Pain Point Analysis",
        "description": "Categorizing customer friction points",
        "model_type": "analysis"
    },
    {
        "id": "journey_mapping",
        "name": "Journey Mapping",
        "description": "Creating customer journey maps",
        "model_type": "analysis"
    }
]


# ===== Journey Stages (5-Stage Model) =====

JOURNEY_STAGES = [
    {
        "id": "awareness",
        "name": "Awareness",
        "objective": "Problem recognition",
        "customer_state": "Experiencing symptoms, not yet searching"
    },
    {
        "id": "consideration",
        "name": "Consideration", 
        "objective": "Solution research",
        "customer_state": "Knows problem, researching solution types"
    },
    {
        "id": "decision",
        "name": "Decision",
        "objective": "Vendor selection",
        "customer_state": "Comparing specific vendors"
    },
    {
        "id": "onboarding",
        "name": "Onboarding",
        "objective": "First value achievement",
        "customer_state": "Implementation and activation"
    },
    {
        "id": "expansion",
        "name": "Expansion",
        "objective": "Maximize lifetime value",
        "customer_state": "Satisfied, ready for more"
    }
]


def get_model_config(model_id: str) -> ModelConfig:
    """Get configuration for a specific model."""
    if model_id not in AVAILABLE_MODELS:
        raise ValueError(f"Unknown model: {model_id}")
    return AVAILABLE_MODELS[model_id]


def calculate_cost(model_id: str, input_tokens: int, output_tokens: int) -> float:
    """Calculate cost for a model request."""
    config = get_model_config(model_id)
    input_cost = (input_tokens / 1_000_000) * config.input_price_per_million
    output_cost = (output_tokens / 1_000_000) * config.output_price_per_million
    return input_cost + output_cost