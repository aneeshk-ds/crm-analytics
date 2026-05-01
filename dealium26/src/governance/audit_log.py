"""In-memory audit log records for demo actions."""

from __future__ import annotations

from datetime import datetime, timezone


def build_audit_entry(query: str, intent: str, action: str, approved: bool) -> dict[str, str | bool]:
    return {
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "query": query,
        "intent": intent,
        "action": action,
        "approved": approved,
    }
