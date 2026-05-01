"""Multilingual output helpers for EN/HI/TE."""

from __future__ import annotations


TEMPLATES = {
    "en": "Found {count} customers. Avg churn risk: {avg_churn_risk}. Top segment: {top_segment}.",
    "hi": "{count} ग्राहक मिले। औसत churn risk: {avg_churn_risk}. प्रमुख segment: {top_segment}.",
    "te": "{count} customers కనుగొన్నారు. సగటు churn risk: {avg_churn_risk}. ప్రధాన segment: {top_segment}.",
}


def render_summary(summary: dict[str, str | int | float], language: str) -> str:
    template = TEMPLATES.get(language, TEMPLATES["en"])
    return template.format(**summary)
