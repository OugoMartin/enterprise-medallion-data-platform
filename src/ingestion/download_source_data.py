"""Download the two large upstream Jaffle Shop CSV files from dbt Labs.
Run from the repository root: python src/ingestion/download_source_data.py
"""
from pathlib import Path
from urllib.request import urlretrieve

BASE="https://raw.githubusercontent.com/dbt-labs/jaffle-shop/main/seeds/jaffle-data"
OUT=Path("data/raw")
FILES=["raw_orders.csv","raw_items.csv"]

def main():
    OUT.mkdir(parents=True,exist_ok=True)
    for name in FILES:
        dest=OUT/name
        print(f"Downloading {name} ...")
        urlretrieve(f"{BASE}/{name}",dest)
        print(f"Saved {dest} ({dest.stat().st_size:,} bytes)")

if __name__=="__main__": main()
