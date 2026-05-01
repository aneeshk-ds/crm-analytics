"""Next-best-action suggestion based on query intent and risk."""

from __future__ import annotations


def suggest_action(intent: str, high_risk_count: int) -> str:
    if intent == "support":
        return "Prioritize unresolved high-risk tickets and assign SLA follow-ups."
    if intent == "sales":
        return "Assign hot leads to reps with 24-hour follow-up tasks."
    if intent == "marketing":
        return "Launch retention outreach to high-risk segments in selected city."
    if high_risk_count > 0:
        return "Review high-risk customers and trigger proactive outreach."
    return "No urgent action required; continue monitoring trends."
