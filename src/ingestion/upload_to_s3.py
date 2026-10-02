from __future__ import annotations

import os
from pathlib import Path

import boto3
from dotenv import load_dotenv

load_dotenv()


def upload_file(file_path: str | Path, dataset: str, bucket: str | None = None) -> str:
    path = Path(file_path)
    bucket_name = bucket or os.getenv("S3_BUCKET")
    if not bucket_name:
        raise ValueError("S3_BUCKET is not configured")
    if not path.exists():
        raise FileNotFoundError(path)

    key = f"landing/{dataset}/{path.name}"
    boto3.client("s3").upload_file(str(path), bucket_name, key)
    return f"s3://{bucket_name}/{key}"
