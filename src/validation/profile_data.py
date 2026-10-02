from pathlib import Path
import pandas as pd

DATA_DIR = Path("data/raw")


def profile_file(file_path: Path) -> dict[str, object]:
    df = pd.read_csv(file_path)
    return {
        "file": file_path.name,
        "rows": len(df),
        "columns": len(df.columns),
        "column_names": df.columns.tolist(),
        "data_types": {c: str(t) for c, t in df.dtypes.items()},
        "missing_values": {c: int(v) for c, v in df.isnull().sum().items()},
        "duplicate_rows": int(df.duplicated().sum()),
    }


def main() -> None:
    files = sorted(DATA_DIR.glob("*.csv"))
    if not files:
        print("No CSV files found in data/raw.")
        return
    for file_path in files:
        print(profile_file(file_path))


if __name__ == "__main__":
    main()
