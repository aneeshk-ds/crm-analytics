"""Data loading utilities for Dealium26."""

from __future__ import annotations

from pathlib import Path
import pandas as pd

REQUIRED_COLUMNS = {
    "customer_id",
    "name",
    "city",
    "state",
    "language_preference",
    "industry",
    "tenure_months",
    "orders_last_90d",
    "aov_inr",
    "total_spend_inr",
    "ticket_count_90d",
    "unresolved_tickets",
    "last_engagement_days",
    "value_score",
    "engagement_score",
    "churn_risk_score",
    "segment",
}


def load_customers(csv_path: str | Path) -> pd.DataFrame:
    frame = pd.read_csv(csv_path)
    missing = REQUIRED_COLUMNS.difference(frame.columns)
    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")
    return frame
