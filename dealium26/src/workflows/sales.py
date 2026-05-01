"""Sales workflow recommendations."""

from __future__ import annotations

import pandas as pd


def build_sales_actions(df: pd.DataFrame) -> list[str]:
    if df.empty:
        return ["No sales actions required."]

    actions: list[str] = []
    high_value = df[df["value_score"] >= 75]
    if not high_value.empty:
        actions.append(f"Assign priority follow-up for {len(high_value)} high-value customers.")

    low_engagement = df[df["engagement_score"] < 45]
    if not low_engagement.empty:
        actions.append(f"Trigger re-engagement outreach for {len(low_engagement)} low-engagement customers.")

    return actions or ["Pipeline healthy; continue weekly cadence."]
