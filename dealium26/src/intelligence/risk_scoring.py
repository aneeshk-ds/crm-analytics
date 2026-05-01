"""Risk labels for customer cohorts."""

from __future__ import annotations

import pandas as pd


def add_risk_band(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()
    out["risk_band"] = pd.cut(
        out["churn_risk_score"],
        bins=[-1, 39, 69, 100],
        labels=["low", "medium", "high"],
    )
    return out
