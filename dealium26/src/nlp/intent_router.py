"""Route user query to top-level CRM intent."""

from __future__ import annotations

INTENT_KEYWORDS = {
    "support": ["ticket", "issue", "complaint", "support", "resolve"],
    "sales": ["lead", "deal", "follow-up", "follow up", "conversion", "upsell"],
    "marketing": ["campaign", "segment", "engagement", "dormant", "churn"],
}


def route_intent(query: str) -> str:
    q = query.lower()
    for intent, words in INTENT_KEYWORDS.items():
        if any(word in q for word in words):
            return intent
    return "general"
