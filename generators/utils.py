#!/usr/bin/env python3
"""
Shared utilities for Cultural Monad generators.

ARCHITECTURE RATIONALE:
Each generator is a true monad - an isolated unit that:
- Contains its own prompt logic (the unique "soul")
- Defines its own output structure (the unique "form")
- Interfaces with the world through this module (the shared protocol)

This enables:
- Add generators without understanding the system (just define prompt + fields + formatter)
- Fix once, fix everywhere (parsing bugs, logging, etc.)
- Swap implementations without touching generators (retry logic, new providers)
- Test core separately from generator-specific prompts
- Compose generators as building blocks with predictable interfaces

No inheritance hierarchies, no framework lock-in, no magic.
Generators can still run standalone (python wizard.py).
Clear boundaries: prompts in generators, infrastructure here.
"""

import os
import sys
import json
from datetime import datetime
from typing import Optional, Callable, Any, List, Tuple

# Ensure llm_client is importable from parent directory
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from llm_client import (
    get_llm_client,
    get_default_model,
    get_completion_params,
    clean_json_response
)

# Re-export for generators - single import point
__all__ = [
    # From llm_client
    'get_llm_client',
    'get_default_model',
    'get_completion_params',
    'clean_json_response',
    # New utilities
    'parse_llm_json_response',
    'save_output',
    'run_generation',
    'check_api_key'
]


def parse_llm_json_response(
    content: str,
    possible_keys: Optional[List[str]] = None
) -> Tuple[Optional[List], Optional[str]]:
    """
    Parse JSON from LLM response with fallback logic for various structures.

    LLMs return JSON in unpredictable wrappers - sometimes bare arrays,
    sometimes {"demographics": [...]}, sometimes {"data": {...}}.
    This handles all cases with a priority-ordered key search.

    Args:
        content: Raw LLM response content (may include markdown fences)
        possible_keys: Keys that might contain the array we want
                      (e.g., ["demographics", "profiles", "personas"])

    Returns:
        Tuple of (parsed_items, error_message)
        Success: (list_of_items, None)
        Failure: (None, error_string)
    """
    if possible_keys is None:
        possible_keys = ["items", "data", "results"]

    # Strip markdown code fences and clean whitespace
    content = clean_json_response(content)

    try:
        data = json.loads(content)

        # Case 1: Already a list
        if isinstance(data, list):
            return data, None

        # Case 2: Dict with known key
        if isinstance(data, dict):
            for key in possible_keys:
                if key in data:
                    return data[key], None

            # Case 3: Dict with unknown key containing a list
            for value in data.values():
                if isinstance(value, list):
                    return value, None

            # Case 4: Single object - wrap in list
            return [data], None

        return None, f"Unexpected response type: {type(data)}"

    except json.JSONDecodeError as e:
        preview = content[:500] if content else "(empty)"
        return None, f"JSON parse error: {e}\nPreview: {preview}..."


def save_output(
    data: dict,
    prefix: str,
    format_markdown: Callable[[dict, Any], None],
    output_format: str = "markdown"
) -> str:
    """
    Save generated data to file with consistent naming and encoding.

    Args:
        data: The complete result dict to save
        prefix: Filename prefix (e.g., "wizard_demographics", "x_aphorisms")
        format_markdown: Function(data, file_handle) that writes markdown content
        output_format: "markdown" or "json"

    Returns:
        Filename of saved file
    """
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    if output_format == "json":
        filename = f"{prefix}_{timestamp}.json"
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
    else:
        filename = f"{prefix}_{timestamp}.md"
        with open(filename, "w", encoding="utf-8") as f:
            format_markdown(data, f)

    print(f"Saved to {filename}")
    return filename


def check_api_key() -> bool:
    """
    Verify API key is configured for the selected LLM provider.

    Returns:
        True if key is set, False otherwise (with error message printed)
    """
    provider = os.getenv("LLM_PROVIDER", "openai").lower()

    if provider == "openrouter":
        if not os.getenv("OPENROUTER_API_KEY"):
            print("Error: OPENROUTER_API_KEY not set")
            print("Get one at: https://openrouter.ai/keys")
            return False
    else:
        if not os.getenv("OPENAI_API_KEY"):
            print("Error: OPENAI_API_KEY not set")
            return False

    return True


def run_generation(
    generate_func: Callable,
    save_func: Callable,
    success_message: str = "Generation complete!",
    **generate_kwargs
) -> bool:
    """
    Standard main() execution pattern for generators.

    Handles API key check, generation, dual-format saving, and messaging.
    Generators call this from main() with their specific functions.

    Args:
        generate_func: The generation function to call
        save_func: The save function to call (called twice: markdown + json)
        success_message: Message to print on success
        **generate_kwargs: Arguments to pass to generate_func

    Returns:
        True on success, False on failure
    """
    if not check_api_key():
        return False

    data = generate_func(**generate_kwargs)

    if data:
        print("\nSaving results...\n")
        save_func(data, output_format="markdown")
        save_func(data, output_format="json")
        print(f"\n{success_message}")
        return True
    else:
        print("Generation failed")
        return False
