from pathlib import Path

from src.ingestion.prepare_data import prepare_file


def test_prepare_file_adds_ingestion_metadata(tmp_path: Path):
    source = tmp_path / "customers.csv"
    source.write_text("customer_id,name\n1,Ada\n", encoding="utf-8")

    df = prepare_file(source, batch_id="batch-test")

    assert df.loc[0, "_source_file"] == "customers.csv"
    assert df.loc[0, "_batch_id"] == "batch-test"
    assert "_ingestion_timestamp" in df.columns
