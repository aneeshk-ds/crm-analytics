from src.nlp.normalize_query import normalize_query
from src.query.query_builder import build_filters


def test_build_filters_city_and_churn() -> None:
    normalized = normalize_query("Show churn customers in Hyderabad")
    filters = build_filters(normalized)
    assert filters["city"] == "Hyderabad"
    assert filters["min_churn_risk"] == 70
