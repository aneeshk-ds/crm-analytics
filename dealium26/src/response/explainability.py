"""Explainability helpers for query outputs."""

from __future__ import annotations


def build_explanation(filters: dict[str, str | int], intent: str) -> list[str]:
    lines = [f"Intent detected: {intent}"]
    if not filters:
        lines.append("No explicit filters detected; showing broad top records.")
        return lines

    for key, value in filters.items():
        lines.append(f"Filter applied: {key} = {value}")
    lines.append("Results sorted by churn_risk_score and value_score.")
    return lines
