"""Language detection helpers without external runtime dependency."""

from __future__ import annotations


def _contains_range(text: str, start: int, end: int) -> bool:
    return any(start <= ord(ch) <= end for ch in text)


def detect_language(text: str) -> str:
    # Telugu Unicode block
    if _contains_range(text, 0x0C00, 0x0C7F):
        return "te"
    # Devanagari block (Hindi)
    if _contains_range(text, 0x0900, 0x097F):
        return "hi"
    return "en"
