"""Export helpers for result datasets and audit logs."""

from __future__ import annotations

import io
import pandas as pd


def to_csv_bytes(df: pd.DataFrame) -> bytes:
    buffer = io.StringIO()
    df.to_csv(buffer, index=False)
    return buffer.getvalue().encode("utf-8")
