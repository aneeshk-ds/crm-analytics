"""Execute dataframe queries for customer retrieval."""

from __future__ import annotations

import pandas as pd


def execute_customer_query(customers: pd.DataFrame, filters: dict[str, str | int]) -> pd.DataFrame:
    df = customers.copy()
    if "city" in filters:
        df = df[df["city"] == filters["city"]]
    if "segment" in filters:
        df = df[df["segment"] == filters["segment"]]
    if "min_churn_risk" in filters:
        df = df[df["churn_risk_score"] >= int(filters["min_churn_risk"])]
    if "min_unresolved_tickets" in filters:
        df = df[df["unresolved_tickets"] >= int(filters["min_unresolved_tickets"])]

    return df.sort_values(["churn_risk_score", "value_score"], ascending=[False, False]).head(25)
