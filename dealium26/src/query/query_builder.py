"""Build dataframe filters from normalized query hints."""

from __future__ import annotations


def build_filters(normalized: dict[str, str | None]) -> dict[str, str | int]:
    filters: dict[str, str | int] = {}
    raw = (normalized.get("raw") or "").lower()

    if normalized.get("city"):
        filters["city"] = str(normalized["city"])
    if "high-value" in raw or "high value" in raw:
        filters["segment"] = "high_value_low_engagement"
    if "churn" in raw:
        filters["min_churn_risk"] = 70
    if "unresolved" in raw:
        filters["min_unresolved_tickets"] = 1

    return filters
