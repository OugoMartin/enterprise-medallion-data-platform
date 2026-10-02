select order_id,order_date,customer_id,product_id,store_id,quantity,unit_price,quantity*unit_price gross_sales
from {{ ref('stg_orders') }} where order_status='completed'
