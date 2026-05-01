"""Marketing workflow recommendations."""

from __future__ import annotations

import pandas as pd


def build_marketing_actions(df: pd.DataFrame) -> list[str]:
    if df.empty:
        return ["No marketing actions required."]

    actions: list[str] = []
    segment_counts = df["segment"].value_counts().head(2)
    for segment, count in segment_counts.items():
        actions.append(f"Create campaign for segment '{segment}' targeting {int(count)} customers.")

    churn_pool = df[df["churn_risk_score"] >= 70]
    if not churn_pool.empty:
        actions.append(f"Run retention offer for {len(churn_pool)} churn-risk customers.")

    return actions
