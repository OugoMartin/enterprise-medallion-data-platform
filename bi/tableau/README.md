# Tableau implementation

Connect Tableau to Snowflake GOLD.FACT_SALES and supporting marts/dimensions.

## Sales & Customer Performance dashboard
Sheets: Revenue Trend, Revenue by Store, Product Performance, Top Customers, KPI tiles. Add Order Date, Store, and Product/Category filters and assemble a 16:9 dashboard.

## Calculated fields
```text
Total Revenue: SUM([Gross Sales])
Average Order Value: SUM([Gross Sales]) / COUNTD([Order Id])
Orders: COUNTD([Order Id])
Customers: COUNTD([Customer Id])
```

## Evidence
After building/publishing the dashboard, save the actual dashboard image as `screenshots/tableau-sales-dashboard.png`. Generated mockups must not be labeled as Tableau screenshots.
