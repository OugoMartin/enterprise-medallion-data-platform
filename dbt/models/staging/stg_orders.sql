select trim(order_id) order_id, trim(customer_id) customer_id, trim(product_id) product_id,
trim(store_id) store_id, try_to_date(order_date) order_date, try_to_number(quantity) quantity,
try_to_decimal(unit_price,18,2) unit_price, lower(trim(order_status)) order_status
from {{ source('bronze','raw_orders') }} where order_id is not null
