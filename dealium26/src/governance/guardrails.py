"""Basic approval guardrails for action execution."""

from __future__ import annotations


HIGH_RISK_KEYWORDS = {"escalate", "retention offer", "priority follow-up"}


def requires_approval(action_text: str) -> bool:
    lowered = action_text.lower()
    return any(keyword in lowered for keyword in HIGH_RISK_KEYWORDS)
