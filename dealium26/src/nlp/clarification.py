"""Ask clarifying question when query is underspecified."""

from __future__ import annotations


def needs_clarification(query_text: str) -> bool:
    return len(query_text.strip().split()) < 4


def clarification_prompt() -> str:
    return "Please add one filter like city, segment, or time window."
