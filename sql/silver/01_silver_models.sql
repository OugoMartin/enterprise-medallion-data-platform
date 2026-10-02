CREATE OR REPLACE VIEW ENTERPRISE_MEDALLION_DB.SILVER.CUSTOMERS AS
SELECT DISTINCT TRIM(customer_id) customer_id, TRIM(customer_name) customer_name
FROM ENTERPRISE_MEDALLION_DB.BRONZE.RAW_CUSTOMERS WHERE customer_id IS NOT NULL;

CREATE OR REPLACE VIEW ENTERPRISE_MEDALLION_DB.SILVER.ORDERS AS
SELECT DISTINCT TRIM(order_id) order_id, TRIM(customer_id) customer_id, TRIM(product_id) product_id,
TRIM(store_id) store_id, TRY_TO_DATE(order_date) order_date, TRY_TO_NUMBER(quantity) quantity,
TRY_TO_DECIMAL(unit_price,18,2) unit_price, LOWER(TRIM(order_status)) order_status
FROM ENTERPRISE_MEDALLION_DB.BRONZE.RAW_ORDERS
WHERE order_id IS NOT NULL AND TRY_TO_NUMBER(quantity)>0 AND TRY_TO_DECIMAL(unit_price,18,2)>=0;
