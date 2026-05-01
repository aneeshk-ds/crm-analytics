from src.governance.guardrails import requires_approval
from src.workflows.presets import PRESET_QUERIES


def test_requires_approval_for_high_risk_action() -> None:
    assert requires_approval("Escalate 4 accounts with unresolved_tickets >= 2.")


def test_presets_cover_industries() -> None:
    assert "Retail & E-commerce" in PRESET_QUERIES
    assert "Hospitality & Events" in PRESET_QUERIES
