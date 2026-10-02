from pathlib import Path
import pandas as pd
from src.ingestion import generate_sample_data

def test_generator_creates_consistent_files(tmp_path, monkeypatch):
    monkeypatch.setattr(generate_sample_data,"OUT",tmp_path)
    generate_sample_data.main(customers=10,orders=25)
    customers=pd.read_csv(tmp_path/"customers.csv")
    orders=pd.read_csv(tmp_path/"orders.csv")
    assert len(customers)==10
    assert len(orders)==25
    assert set(orders.customer_id).issubset(set(customers.customer_id))
    assert (orders.quantity>0).all()
