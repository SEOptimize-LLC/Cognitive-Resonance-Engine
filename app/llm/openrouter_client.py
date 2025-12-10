"""
OpenRouter API Client
=====================
Handles all communication with the OpenRouter API for LLM interactions.
"""

import httpx
from typing import Optional, Dict, Any, List
from dataclasses import dataclass, field
from datetime import datetime
from tenacity import (
    retry,
    stop_after_attempt,
    wait_exponential,
    retry_if_exception_type
)
import streamlit as st

from app.config import (
    APP_CONFIG,
    get_model_config,
    calculate_cost,
    DEFAULT_RESEARCH_MODEL,
    DEFAULT_ANALYSIS_MODEL
)


@dataclass
class TokenUsage:
    """Track token usage for a single request."""
    model: str
    input_tokens: int
    output_tokens: int
    total_tokens: int
    estimated_cost: float
    timestamp: datetime = field(default_factory=datetime.now)


@dataclass
class LLMResponse:
    """Response from an LLM request."""
    content: str
    model: str
    usage: TokenUsage
    raw_response: Dict[str, Any]


class CostTracker:
    """Track cumulative costs across the session."""
    
    def __init__(self):
        self.usage_log: List[TokenUsage] = []
    
    def log_usage(self, usage: TokenUsage):
        """Log a token usage record."""
        self.usage_log.append(usage)
    
    def get_total_cost(self) -> float:
        """Get total cost for the session."""
        return sum(u.estimated_cost for u in self.usage_log)
    
    def get_total_tokens(self) -> Dict[str, int]:
        """Get total input and output tokens."""
        return {
            "input": sum(u.input_tokens for u in self.usage_log),
            "output": sum(u.output_tokens for u in self.usage_log),
            "total": sum(u.total_tokens for u in self.usage_log)
        }
    
    def get_usage_by_model(self) -> Dict[str, Dict[str, Any]]:
        """Get usage breakdown by model."""
        breakdown = {}
        for usage in self.usage_log:
            if usage.model not in breakdown:
                breakdown[usage.model] = {
                    "input_tokens": 0,
                    "output_tokens": 0,
                    "total_tokens": 0,
                    "cost": 0.0,
                    "requests": 0
                }
            breakdown[usage.model]["input_tokens"] += usage.input_tokens
            breakdown[usage.model]["output_tokens"] += usage.output_tokens
            breakdown[usage.model]["total_tokens"] += usage.total_tokens
            breakdown[usage.model]["cost"] += usage.estimated_cost
            breakdown[usage.model]["requests"] += 1
        return breakdown
    
    def get_summary(self) -> Dict[str, Any]:
        """Get a complete usage summary."""
        return {
            "total_cost": self.get_total_cost(),
            "total_tokens": self.get_total_tokens(),
            "by_model": self.get_usage_by_model(),
            "total_requests": len(self.usage_log)
        }


class OpenRouterClient:
    """Client for interacting with OpenRouter API."""
    
    def __init__(
        self,
        api_key: Optional[str] = None,
        cost_tracker: Optional[CostTracker] = None
    ):
        """
        Initialize the OpenRouter client.
        
        Args:
            api_key: OpenRouter API key. If not provided, will try to get
                     from Streamlit secrets.
            cost_tracker: Optional cost tracker for logging usage.
        """
        self.api_key = api_key or self._get_api_key()
        self.base_url = APP_CONFIG["openrouter_base_url"]
        self.timeout = APP_CONFIG["request_timeout"]
        self.cost_tracker = cost_tracker or CostTracker()
        
        # HTTP client
        self.client = httpx.Client(
            base_url=self.base_url,
            timeout=self.timeout,
            headers=self._get_headers()
        )
    
    def _get_api_key(self) -> str:
        """Get API key from Streamlit secrets."""
        try:
            # Try flat format first (recommended for Streamlit Cloud)
            if "OPENROUTER_API_KEY" in st.secrets:
                return st.secrets["OPENROUTER_API_KEY"]
            # Try nested format as fallback
            if "api_keys" in st.secrets:
                return st.secrets["api_keys"]["OPENROUTER_API_KEY"]
            raise KeyError("API key not found")
        except (KeyError, FileNotFoundError):
            raise ValueError(
                "OpenRouter API key not found. Please set "
                "OPENROUTER_API_KEY in your Streamlit secrets."
            )
    
    def _get_headers(self) -> Dict[str, str]:
        """Get headers for API requests."""
        return {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
            "HTTP-Referer": "https://cognitive-resonance-engine.streamlit.app",
            "X-Title": "Cognitive Resonance Engine"
        }
    
    @retry(
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=1, min=4, max=10),
        retry=retry_if_exception_type((httpx.TimeoutException, httpx.HTTPStatusError))
    )
    def _make_request(
        self,
        model: str,
        messages: List[Dict[str, str]],
        temperature: float = 0.7,
        max_tokens: Optional[int] = None
    ) -> Dict[str, Any]:
        """
        Make a request to the OpenRouter API.
        
        Args:
            model: Model ID to use
            messages: List of message dicts with 'role' and 'content'
            temperature: Sampling temperature (0-1)
            max_tokens: Maximum tokens in response
            
        Returns:
            Raw API response dict
        """
        model_config = get_model_config(model)
        
        payload = {
            "model": model,
            "messages": messages,
            "temperature": temperature,
        }
        
        if max_tokens:
            payload["max_tokens"] = max_tokens
        else:
            payload["max_tokens"] = model_config.max_tokens
        
        response = self.client.post("/chat/completions", json=payload)
        response.raise_for_status()
        
        return response.json()
    
    def chat(
        self,
        messages: List[Dict[str, str]],
        model: Optional[str] = None,
        temperature: float = 0.7,
        max_tokens: Optional[int] = None,
        system_prompt: Optional[str] = None
    ) -> LLMResponse:
        """
        Send a chat completion request.
        
        Args:
            messages: List of message dicts with 'role' and 'content'
            model: Model ID (defaults to DEFAULT_ANALYSIS_MODEL)
            temperature: Sampling temperature
            max_tokens: Maximum tokens in response
            system_prompt: Optional system prompt to prepend
            
        Returns:
            LLMResponse with content and usage info
        """
        model = model or DEFAULT_ANALYSIS_MODEL
        
        # Prepend system prompt if provided
        if system_prompt:
            messages = [
                {"role": "system", "content": system_prompt}
            ] + messages
        
        # Make request
        raw_response = self._make_request(
            model=model,
            messages=messages,
            temperature=temperature,
            max_tokens=max_tokens
        )
        
        # Extract content
        content = raw_response["choices"][0]["message"]["content"]
        
        # Extract usage
        usage_data = raw_response.get("usage", {})
        input_tokens = usage_data.get("prompt_tokens", 0)
        output_tokens = usage_data.get("completion_tokens", 0)
        total_tokens = usage_data.get("total_tokens", input_tokens + output_tokens)
        
        # Calculate cost
        cost = calculate_cost(model, input_tokens, output_tokens)
        
        # Create usage record
        usage = TokenUsage(
            model=model,
            input_tokens=input_tokens,
            output_tokens=output_tokens,
            total_tokens=total_tokens,
            estimated_cost=cost
        )
        
        # Log usage
        self.cost_tracker.log_usage(usage)
        
        return LLMResponse(
            content=content,
            model=model,
            usage=usage,
            raw_response=raw_response
        )
    
    def research(
        self,
        query: str,
        context: Optional[str] = None,
        model: Optional[str] = None
    ) -> LLMResponse:
        """
        Conduct web research using Perplexity Sonar.
        
        Args:
            query: Research query/question
            context: Optional additional context
            model: Model to use (defaults to Perplexity Sonar)
            
        Returns:
            LLMResponse with research results
        """
        model = model or DEFAULT_RESEARCH_MODEL
        
        messages = []
        if context:
            messages.append({
                "role": "system",
                "content": f"Context: {context}"
            })
        
        messages.append({
            "role": "user",
            "content": query
        })
        
        return self.chat(
            messages=messages,
            model=model,
            temperature=0.3  # Lower temperature for research
        )
    
    def analyze(
        self,
        prompt: str,
        data: Optional[str] = None,
        model: Optional[str] = None,
        system_prompt: Optional[str] = None
    ) -> LLMResponse:
        """
        Run an analysis prompt.
        
        Args:
            prompt: The analysis prompt
            data: Optional data to include in the request
            model: Model to use (defaults to analysis model)
            system_prompt: Optional system prompt
            
        Returns:
            LLMResponse with analysis results
        """
        model = model or DEFAULT_ANALYSIS_MODEL
        
        content = prompt
        if data:
            content = f"{prompt}\n\nDATA:\n{data}"
        
        messages = [{"role": "user", "content": content}]
        
        return self.chat(
            messages=messages,
            model=model,
            temperature=0.7,
            system_prompt=system_prompt
        )
    
    def close(self):
        """Close the HTTP client."""
        self.client.close()
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()


def create_client(
    api_key: Optional[str] = None,
    cost_tracker: Optional[CostTracker] = None
) -> OpenRouterClient:
    """
    Factory function to create an OpenRouter client.
    
    Args:
        api_key: Optional API key
        cost_tracker: Optional cost tracker
        
    Returns:
        Configured OpenRouterClient
    """
    return OpenRouterClient(api_key=api_key, cost_tracker=cost_tracker)