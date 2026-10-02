"""Generate reproducible synthetic transactional data for local pipeline testing.
This is not a substitute for the upstream Jaffle Shop dataset; it enables CI and demos without redistributing third-party data.
"""
from pathlib import Path
import random
import pandas as pd

OUT=Path("data/generated")
SEED=42

def main(customers=500, orders=5000):
    random.seed(SEED); OUT.mkdir(parents=True,exist_ok=True)
    c=pd.DataFrame([{"customer_id":f"C{i:04d}","customer_name":f"Customer {i:04d}"} for i in range(1,customers+1)])
    products=pd.DataFrame([{"product_id":f"P{i:03d}","product_name":f"Product {i:03d}","category":random.choice(["Jaffle","Beverage"]),"unit_price":random.choice([4,5,6,7,11,12,14])} for i in range(1,21)])
    stores=pd.DataFrame([{"store_id":f"S{i:02d}","store_name":n} for i,n in enumerate(["Philadelphia","Brooklyn","Chicago","San Francisco","New Orleans","Los Angeles"],1)])
    rows=[]
    for i in range(1,orders+1):
        p=products.iloc[random.randrange(len(products))]
        qty=random.randint(1,4)
        rows.append({"order_id":f"O{i:06d}","customer_id":random.choice(c.customer_id.tolist()),"product_id":p.product_id,"store_id":random.choice(stores.store_id.tolist()),"order_date":(pd.Timestamp("2024-01-01")+pd.Timedelta(days=random.randint(0,729))).date(),"quantity":qty,"unit_price":p.unit_price,"order_status":random.choice(["completed","completed","completed","cancelled"])})
    for name,df in {"customers":c,"products":products,"stores":stores,"orders":pd.DataFrame(rows)}.items(): df.to_csv(OUT/f"{name}.csv",index=False)
    print({name:len(df) for name,df in {"customers":c,"products":products,"stores":stores,"orders":pd.DataFrame(rows)}.items()})

if __name__=="__main__": main()
