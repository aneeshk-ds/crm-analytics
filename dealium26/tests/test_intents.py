from src.nlp.intent_router import route_intent


def test_route_support_intent() -> None:
    assert route_intent("Show unresolved ticket issues") == "support"


def test_route_sales_intent() -> None:
    assert route_intent("Find hot leads for follow-up") == "sales"
