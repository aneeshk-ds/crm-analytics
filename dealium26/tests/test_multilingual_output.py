from src.response.multilingual_output import render_summary


def test_render_summary_hindi() -> None:
    text = render_summary({"count": 5, "avg_churn_risk": 71.2, "avg_value_score": 64.0, "top_segment": "high_value_low_engagement"}, "hi")
    assert "5" in text
    assert "ग्राहक" in text
