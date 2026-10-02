"""Build a BI-ready CSV for Power BI and Tableau from official Jaffle Shop raw files.
Prices in Jaffle Shop are integer cents; monetary output columns are converted to dollars.
Run after: python src/ingestion/download_source_data.py
Then:      python src/transformation/build_bi_dataset.py
"""
from pathlib import Path
import pandas as pd

RAW=Path("data/raw")
OUT=Path("data/analytics")

def main():
    customers=pd.read_csv(RAW/"raw_customers.csv").rename(columns={"id":"customer_id","name":"customer_name"})
    orders=pd.read_csv(RAW/"raw_orders.csv").rename(columns={"id":"order_id","customer":"customer_id"})
    items=pd.read_csv(RAW/"raw_items.csv").rename(columns={"id":"order_item_id"})
    products=pd.read_csv(RAW/"raw_products.csv").rename(columns={"name":"product_name","type":"product_type"})
    stores=pd.read_csv(RAW/"raw_stores.csv").rename(columns={"id":"store_id","name":"store_name"})

    df=(items.merge(orders,on="order_id",how="left",validate="many_to_one")
             .merge(customers,on="customer_id",how="left",validate="many_to_one")
             .merge(products,on="sku",how="left",validate="many_to_one")
             .merge(stores,on="store_id",how="left",validate="many_to_one"))
    df["ordered_at"]=pd.to_datetime(df["ordered_at"],errors="coerce")
    df["order_date"]=df["ordered_at"].dt.date
    df["year"]=df["ordered_at"].dt.year
    df["month"]=df["ordered_at"].dt.month
    df["month_name"]=df["ordered_at"].dt.month_name()
    df["year_month"]=df["ordered_at"].dt.to_period("M").astype(str)
    df["product_price"]=pd.to_numeric(df["price"],errors="coerce")/100
    for col in ["subtotal","tax_paid","order_total"]:
        df[col]=pd.to_numeric(df[col],errors="coerce")/100
    df["line_revenue"]=df["product_price"]
    cols=["order_item_id","order_id","order_date","ordered_at","year","month","month_name","year_month","customer_id","customer_name","store_id","store_name","sku","product_name","product_type","product_price","line_revenue","subtotal","tax_paid","order_total","tax_rate"]
    OUT.mkdir(parents=True,exist_ok=True)
    dest=OUT/"jaffle_sales_analytics.csv"
    df[cols].to_csv(dest,index=False)
    print(f"Created {dest}: {len(df):,} rows, {len(cols)} columns")

if __name__=="__main__": main()
