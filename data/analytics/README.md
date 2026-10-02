# Analytics data for Power BI and Tableau

Generate the shared BI dataset from the official Jaffle Shop raw files:

```bash
python src/ingestion/download_source_data.py
python src/transformation/build_bi_dataset.py
```

Output: `data/analytics/jaffle_sales_analytics.csv`.

## Grain
One row per order item. This grain supports product analysis without double-counting item rows. Order-level measures such as `order_total` repeat across items, so use distinct-order logic for order-level KPIs or use `line_revenue` for additive product/store analysis.

## BI fields
Order identifiers/dates, customer, store, SKU/product/type, product price/line revenue, subtotal, tax, order total, and calendar helper fields (year, month, month name, year-month).

Jaffle Shop source monetary values are stored as integer cents; the builder converts them to dollars for BI use.
