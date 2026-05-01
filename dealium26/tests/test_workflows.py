import pytest

pd = pytest.importorskip("pandas")

from src.workflows.marketing import build_marketing_actions
from src.workflows.sales import build_sales_actions
from src.workflows.support import build_support_actions


def _sample_df():
    return pd.DataFrame(
        {
            "unresolved_tickets": [3, 0, 1],
            "risk_band": ["high", "low", "high"],
            "value_score": [80, 50, 76],
            "engagement_score": [30, 60, 40],
            "segment": ["high_value_low_engagement", "mid_value_growth", "high_value_low_engagement"],
            "churn_risk_score": [88, 35, 75],
        }
    )


def test_support_actions() -> None:
    actions = build_support_actions(_sample_df())
    assert any("Escalate" in a for a in actions)


def test_sales_actions() -> None:
    actions = build_sales_actions(_sample_df())
    assert any("priority follow-up" in a for a in actions)


def test_marketing_actions() -> None:
    actions = build_marketing_actions(_sample_df())
    assert any("campaign" in a for a in actions)
