with customers as (

  SELECT distinct id as customer_id, 
      first_name, 
      last_name
  from {{ source('jaffle_shop', 'customers') }}
)

select * from customers