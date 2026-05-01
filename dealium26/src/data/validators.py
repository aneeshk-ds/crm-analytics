"""Data validation checks for mock CRM data."""

from __future__ import annotations

import pandas as pd


def basic_quality_report(df: pd.DataFrame) -> dict[str, float]:
    duplicate_ratio = float(df.duplicated(subset=["customer_id"]).mean())
    missing_ratio = float(df.isna().mean().mean())
    stale_ratio = float((df["last_engagement_days"] > 60).mean())
    unresolved_ratio = float((df["unresolved_tickets"] > 0).mean())
    return {
        "duplicate_ratio": round(duplicate_ratio, 4),
        "missing_ratio": round(missing_ratio, 4),
        "stale_ratio": round(stale_ratio, 4),
        "unresolved_ratio": round(unresolved_ratio, 4),
    }
