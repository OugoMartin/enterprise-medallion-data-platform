from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
from uuid import uuid4

import pandas as pd


def prepare_file(file_path: str | Path, batch_id: str | None = None) -> pd.DataFrame:
    path = Path(file_path)
    df = pd.read_csv(path)
    df["_source_file"] = path.name
    df["_batch_id"] = batch_id or str(uuid4())
    df["_ingestion_timestamp"] = datetime.now(timezone.utc)
    return df
