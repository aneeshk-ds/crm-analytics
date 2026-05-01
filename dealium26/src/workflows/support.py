"""Support workflow recommendations."""

from __future__ import annotations

import pandas as pd


def build_support_actions(df: pd.DataFrame) -> list[str]:
    if df.empty:
        return ["No support actions required."]

    actions: list[str] = []
    urgent = df[df["unresolved_tickets"] >= 2]
    if not urgent.empty:
        actions.append(f"Escalate {len(urgent)} accounts with unresolved_tickets >= 2.")

    high_risk = df[df["risk_band"] == "high"]
    if not high_risk.empty:
        actions.append(f"Create callback tasks for {len(high_risk)} high-risk customers.")

    return actions or ["Monitor support queue; no critical signals."]
