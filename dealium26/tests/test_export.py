import pytest

pd = pytest.importorskip("pandas")

from src.response.export import to_csv_bytes


def test_to_csv_bytes() -> None:
    df = pd.DataFrame({"a": [1], "b": ["x"]})
    payload = to_csv_bytes(df)
    assert b"a,b" in payload
