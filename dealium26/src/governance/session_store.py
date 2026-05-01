"""Session-level history storage helpers."""

from __future__ import annotations

import streamlit as st


def get_history() -> list[dict]:
    if "history" not in st.session_state:
        st.session_state["history"] = []
    return st.session_state["history"]


def add_history(entry: dict) -> None:
    history = get_history()
    history.append(entry)
