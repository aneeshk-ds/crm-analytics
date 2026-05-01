"""Response formatting utilities."""

from __future__ import annotations

import pandas as pd


def summarize_results(df: pd.DataFrame) -> dict[str, str | int | float]:
    if df.empty:
        return {
            "count": 0,
            "avg_churn_risk": 0.0,
            "avg_value_score": 0.0,
            "top_segment": "none",
        }

    return {
        "count": int(len(df)),
        "avg_churn_risk": round(float(df["churn_risk_score"].mean()), 2),
        "avg_value_score": round(float(df["value_score"].mean()), 2),
        "top_segment": str(df["segment"].mode().iloc[0]),
    }
