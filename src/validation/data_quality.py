from __future__ import annotations

import pandas as pd


def check_nulls(df: pd.DataFrame) -> dict[str, int]:
    return {column: int(count) for column, count in df.isnull().sum().items()}


def check_duplicates(df: pd.DataFrame) -> int:
    return int(df.duplicated().sum())


def check_schema(df: pd.DataFrame, required_columns: list[str]) -> dict[str, object]:
    missing = [column for column in required_columns if column not in df.columns]
    return {"valid": not missing, "missing_columns": missing}


def validate_dataset(df: pd.DataFrame, required_columns: list[str]) -> dict[str, object]:
    return {
        "row_count": int(len(df)),
        "duplicate_count": check_duplicates(df),
        "null_counts": check_nulls(df),
        "schema": check_schema(df, required_columns),
    }
