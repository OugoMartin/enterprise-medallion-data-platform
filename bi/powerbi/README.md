# Power BI implementation

Connect Power BI to Snowflake and use the GOLD schema. Primary tables are FACT_SALES, MART_DAILY_SALES, MART_CUSTOMER_VALUE plus product/store dimensions when implemented.

## Executive Sales Performance page
KPI cards: Total Revenue, Total Orders, Average Order Value, Unique Customers.
Visuals: monthly revenue trend; revenue by store; product/category performance; top customers; date/store/category slicers.

## Core DAX
```DAX
Total Revenue = SUM(FACT_SALES[gross_sales])
Total Orders = DISTINCTCOUNT(FACT_SALES[order_id])
Average Order Value = DIVIDE([Total Revenue], [Total Orders])
Unique Customers = DISTINCTCOUNT(FACT_SALES[customer_id])
Units Sold = SUM(FACT_SALES[quantity])
```

## Evidence
After building the report in Power BI Desktop, export the actual report page to `screenshots/powerbi-sales-dashboard.png`. Generated mockups must not be labeled as Power BI screenshots.
