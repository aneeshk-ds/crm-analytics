import pytest

pd = pytest.importorskip("pandas")

from src.intelligence.next_best_action import suggest_action
from src.response.formatter import summarize_results


def test_summarize_results_non_empty() -> None:
    frame = pd.DataFrame(
        {
            "churn_risk_score": [70.0, 80.0],
            "value_score": [60.0, 90.0],
            "segment": ["a", "a"],
        }
    )
    summary = summarize_results(frame)
    assert summary["count"] == 2
    assert summary["top_segment"] == "a"


def test_suggest_action_support() -> None:
    assert "SLA" in suggest_action("support", 3)
