"""Generate India-focused mock CRM datasets for Dealium26 MVP."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import random

import numpy as np
import pandas as pd


@dataclass
class GeneratorConfig:
    seed: int = 26
    n_customers: int = 500


CITIES = [
    ("Bengaluru", "Karnataka", "te"),
    ("Hyderabad", "Telangana", "te"),
    ("Mumbai", "Maharashtra", "en"),
    ("Delhi", "Delhi", "hi"),
    ("Pune", "Maharashtra", "en"),
    ("Chennai", "Tamil Nadu", "en"),
    ("Ahmedabad", "Gujarat", "hi"),
    ("Kolkata", "West Bengal", "en"),
]

INDUSTRIES = [
    "Retail & E-commerce",
    "Real Estate",
    "Manufacturing / Trading / B2B",
    "Education & Coaching",
    "Healthcare & Wellness",
    "Logistics / Transport / Travel",
    "Service Businesses & Agencies",
    "Home Services & Construction",
    "Hospitality & Events",
]


def _segment_from_scores(value_score: float, engagement_score: float) -> str:
    if value_score >= 75 and engagement_score >= 60:
        return "high_value_engaged"
    if value_score >= 75 and engagement_score < 60:
        return "high_value_low_engagement"
    if value_score < 40 and engagement_score < 40:
        return "low_value_at_risk"
    return "mid_value_growth"


def generate_customers(config: GeneratorConfig | None = None) -> pd.DataFrame:
    config = config or GeneratorConfig()
    random.seed(config.seed)
    np.random.seed(config.seed)

    rows: list[dict] = []
    for i in range(config.n_customers):
        city, state, default_lang = random.choice(CITIES)
        value_score = float(np.clip(np.random.normal(58, 20), 5, 99))
        engagement_score = float(np.clip(np.random.normal(54, 24), 2, 99))
        recency_days = int(np.clip(np.random.exponential(25), 0, 180))
        churn_risk = float(np.clip((100 - engagement_score) * 0.6 + recency_days * 0.3, 1, 99))

        rows.append(
            {
                "customer_id": f"CUST{i + 1:05d}",
                "name": f"Customer {i + 1}",
                "city": city,
                "state": state,
                "language_preference": random.choices([default_lang, "en", "hi", "te"], [0.5, 0.2, 0.2, 0.1])[0],
                "industry": random.choice(INDUSTRIES),
                "tenure_months": int(np.clip(np.random.normal(24, 14), 1, 120)),
                "orders_last_90d": int(np.clip(np.random.poisson(4), 0, 30)),
                "aov_inr": int(np.clip(np.random.normal(2400, 1800), 200, 18000)),
                "total_spend_inr": int(np.clip(np.random.normal(56000, 35000), 1000, 500000)),
                "ticket_count_90d": int(np.clip(np.random.poisson(1.6), 0, 12)),
                "unresolved_tickets": int(np.clip(np.random.poisson(0.5), 0, 8)),
                "last_engagement_days": recency_days,
                "value_score": round(value_score, 2),
                "engagement_score": round(engagement_score, 2),
                "churn_risk_score": round(churn_risk, 2),
                "segment": _segment_from_scores(value_score, engagement_score),
            }
        )

    return pd.DataFrame(rows)


def save_mock_dataset(output_dir: str | Path, config: GeneratorConfig | None = None) -> Path:
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    customers = generate_customers(config)
    file_path = output_path / "customers.csv"
    customers.to_csv(file_path, index=False)
    return file_path
