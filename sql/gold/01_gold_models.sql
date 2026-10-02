CREATE OR REPLACE VIEW ENTERPRISE_MEDALLION_DB.GOLD.FACT_SALES AS
SELECT o.order_id,o.order_date,o.customer_id,o.product_id,o.store_id,o.quantity,o.unit_price,
       o.quantity*o.unit_price AS gross_sales
FROM ENTERPRISE_MEDALLION_DB.SILVER.ORDERS o WHERE o.order_status='completed';

CREATE OR REPLACE VIEW ENTERPRISE_MEDALLION_DB.GOLD.MART_DAILY_SALES AS
SELECT order_date, COUNT(DISTINCT order_id) total_orders, SUM(quantity) units_sold,
       SUM(gross_sales) total_revenue, total_revenue/NULLIF(total_orders,0) average_order_value
FROM ENTERPRISE_MEDALLION_DB.GOLD.FACT_SALES GROUP BY order_date;

CREATE OR REPLACE VIEW ENTERPRISE_MEDALLION_DB.GOLD.MART_CUSTOMER_VALUE AS
SELECT customer_id,COUNT(DISTINCT order_id) orders,SUM(gross_sales) lifetime_revenue,
       MAX(order_date) last_order_date
FROM ENTERPRISE_MEDALLION_DB.GOLD.FACT_SALES GROUP BY customer_id;
