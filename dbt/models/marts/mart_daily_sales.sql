select order_date,count(distinct order_id) total_orders,sum(quantity) units_sold,sum(gross_sales) total_revenue,
sum(gross_sales)/nullif(count(distinct order_id),0) average_order_value
from {{ ref('fact_sales') }} group by order_date
