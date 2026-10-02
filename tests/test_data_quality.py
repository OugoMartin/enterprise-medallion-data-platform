import pandas as pd

from src.validation.data_quality import check_duplicates, check_nulls, check_schema, validate_dataset


def sample_df():
    return pd.DataFrame({"id": [1, 2, 2], "status": ["paid", None, None]})


def test_null_counts():
    assert check_nulls(sample_df())["status"] == 2


def test_duplicate_count():
    df = pd.DataFrame({"id": [1, 1], "value": ["a", "a"]})
    assert check_duplicates(df) == 1


def test_schema_detects_missing_columns():
    result = check_schema(sample_df(), ["id", "status", "amount"])
    assert result == {"valid": False, "missing_columns": ["amount"]}


def test_validate_dataset_returns_core_metrics():
    result = validate_dataset(sample_df(), ["id", "status"])
    assert result["row_count"] == 3
    assert result["schema"]["valid"] is True
