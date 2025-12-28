#!/usr/bin/env python3
"""
Unified LLM Client for Cultural Monad Optimization System
Supports OpenAI, OpenRouter, and other OpenAI-compatible providers
"""

import os
from openai import OpenAI


def get_llm_client(provider: str = None, api_key: str = None, model: str = None):
    """
    Get an LLM client configured for the specified provider.

    Args:
        provider: "openai" or "openrouter" (defaults to env var LLM_PROVIDER or "openai")
        api_key: API key (defaults to env var based on provider)
        model: Model name (for reference, not used in client creation)

    Returns:
        OpenAI client configured for the specified provider
    """

    # Determine provider
    if provider is None:
        provider = os.getenv("LLM_PROVIDER", "openai").lower()

    if provider == "openrouter":
        # OpenRouter configuration
        base_url = "https://openrouter.ai/api/v1"
        api_key = api_key or os.getenv("OPENROUTER_API_KEY")

        if not api_key:
            raise ValueError(
                "OpenRouter API key not found. "
                "Set OPENROUTER_API_KEY in .env.local or pass api_key parameter"
            )

        # OpenRouter uses OpenAI-compatible API but with custom headers
        client = OpenAI(
            base_url=base_url,
            api_key=api_key,
            default_headers={
                "HTTP-Referer": os.getenv("OPENROUTER_REFERER", "https://github.com/your-repo"),
                "X-Title": os.getenv("OPENROUTER_TITLE", "Cultural Monad Optimization System")
            }
        )

        return client

    elif provider == "openai":
        # OpenAI configuration
        api_key = api_key or os.getenv("OPENAI_API_KEY")

        if not api_key:
            raise ValueError(
                "OpenAI API key not found. "
                "Set OPENAI_API_KEY in .env.local or pass api_key parameter"
            )

        client = OpenAI(api_key=api_key)
        return client

    else:
        raise ValueError(f"Unsupported provider: {provider}. Use 'openai' or 'openrouter'")


def get_default_model(provider: str = None):
    """
    Get the default model for the specified provider.

    Args:
        provider: "openai" or "openrouter" (defaults to env var LLM_PROVIDER)

    Returns:
        Default model name string
    """

    if provider is None:
        provider = os.getenv("LLM_PROVIDER", "openai").lower()

    # Check for explicit model override first
    model_override = os.getenv("LLM_MODEL")
    if model_override:
        return model_override

    if provider == "openrouter":
        # OpenRouter models - great for creative writing!
        # Some recommended models:
        # - anthropic/claude-3.5-sonnet (excellent for creative writing)
        # - anthropic/claude-3-opus (top-tier creative writing)
        # - google/gemini-pro-1.5 (great for creative tasks)
        # - meta-llama/llama-3.1-70b-instruct (strong open-source option)
        return os.getenv("OPENROUTER_DEFAULT_MODEL", "anthropic/claude-3.5-sonnet")

    elif provider == "openai":
        return os.getenv("OPENAI_DEFAULT_MODEL", "gpt-4o")

    else:
        return "gpt-4o"


# Popular OpenRouter models for reference
OPENROUTER_MODELS = {
    # Anthropic Claude (excellent for creative writing)
    "claude-3.5-sonnet": "anthropic/claude-3.5-sonnet",
    "claude-3-opus": "anthropic/claude-3-opus",
    "claude-3-sonnet": "anthropic/claude-3-sonnet",
    "claude-3-haiku": "anthropic/claude-3-haiku",

    # Google Gemini
    "gemini-pro-1.5": "google/gemini-pro-1.5",
    "gemini-flash-1.5": "google/gemini-flash-1.5",

    # Meta Llama
    "llama-3.1-405b": "meta-llama/llama-3.1-405b-instruct",
    "llama-3.1-70b": "meta-llama/llama-3.1-70b-instruct",
    "llama-3.1-8b": "meta-llama/llama-3.1-8b-instruct",

    # Mistral
    "mistral-large": "mistralai/mistral-large",
    "mistral-medium": "mistralai/mistral-medium",

    # Moonshot AI (great for creative Chinese/multilingual content)
    "kimi-k2": "moonshotai/kimi-k2-0905",

    # Other interesting models
    "qwen-2.5-72b": "qwen/qwen-2.5-72b-instruct",
    "deepseek-chat": "deepseek/deepseek-chat",
    "thedrummer-anubis": "thedrummer/anubis-70b-v1.1"
}


def get_available_models(provider: str = None):
    """
    Get list of available models for the provider.

    Args:
        provider: "openai" or "openrouter"

    Returns:
        Dictionary of model aliases to full model names
    """

    if provider is None:
        provider = os.getenv("LLM_PROVIDER", "openai").lower()

    if provider == "openrouter":
        return OPENROUTER_MODELS
    elif provider == "openai":
        return {
            "gpt-4o": "gpt-4o",
            "gpt-4-turbo": "gpt-4-turbo-preview",
            "gpt-3.5-turbo": "gpt-3.5-turbo",
            "o3-mini": "o3-mini-2025-01-31",
            "o3": "o3-2025-04-16"
        }
    else:
        return {}


def get_completion_params(model: str, max_tokens: int = 4000, temperature: float = 0.7):
    """
    Get model-appropriate completion parameters.

    Different models support different parameters:
    - o3 models: max_completion_tokens, no temperature
    - Most models: max_tokens, temperature
    - Some models don't support response_format

    Args:
        model: Model name
        max_tokens: Maximum tokens to generate
        temperature: Sampling temperature (ignored for o3)

    Returns:
        Dictionary of parameters to pass to chat.completions.create()
    """
    params = {}

    # Handle o3 models specially
    if "o3" in model.lower():
        params["max_completion_tokens"] = max_tokens
        # o3 doesn't support temperature parameter
    else:
        params["max_tokens"] = max_tokens
        params["temperature"] = temperature

    # Some models don't support response_format
    # Currently known: Moonshot (Kimi), DeepSeek, Qwen
    models_without_response_format = ["moonshot", "kimi", "deepseek", "qwen"]
    if not any(name in model.lower() for name in models_without_response_format):
        params["response_format"] = {"type": "json_object"}

    return params


def clean_json_response(content: str) -> str:
    """
    Clean JSON response by removing markdown code fences and extra whitespace.

    Some models (especially via OpenRouter) wrap JSON in markdown code blocks:
    ```json
    {...}
    ```

    This function strips those fences to return clean JSON.

    Args:
        content: Raw response content from LLM

    Returns:
        Cleaned JSON string
    """
    # Remove markdown code fences
    content = content.strip()

    # Check for code fence patterns
    if content.startswith("```"):
        # Remove opening fence (```json or just ```)
        lines = content.split('\n')
        if lines[0].startswith("```"):
            lines = lines[1:]

        # Remove closing fence
        if lines and lines[-1].strip() == "```":
            lines = lines[:-1]

        content = '\n'.join(lines)

    return content.strip()
