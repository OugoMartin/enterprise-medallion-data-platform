select distinct trim(customer_id) as customer_id, trim(customer_name) as customer_name
from {{ source('bronze','raw_customers') }} where customer_id is not null
