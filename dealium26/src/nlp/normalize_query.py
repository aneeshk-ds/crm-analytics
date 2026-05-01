"""Normalize multilingual prompts into internal analysis hints."""

from __future__ import annotations

from src.nlp.language_detect import detect_language


CITY_ALIASES = {
    "bangalore": "Bengaluru",
    "bengaluru": "Bengaluru",
    "hyderabad": "Hyderabad",
    "mumbai": "Mumbai",
    "delhi": "Delhi",
    "pune": "Pune",
    "chennai": "Chennai",
    "ahmedabad": "Ahmedabad",
    "kolkata": "Kolkata",
}


def normalize_query(text: str) -> dict[str, str | None]:
    lowered = text.lower()
    city = None
    for alias, canonical in CITY_ALIASES.items():
        if alias in lowered:
            city = canonical
            break

    return {
        "raw": text,
        "language": detect_language(text),
        "city": city,
    }
