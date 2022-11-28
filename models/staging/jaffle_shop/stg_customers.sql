with customers as (

  SELECT id as customer_id, 
      first_name, 
      last_name, 
      COUNT(*) AS cnt
  FROM raw.jaffle_shop.customers
  GROUP BY customer_id, 
        first_name, 
        last_name
  HAVING COUNT(*) > 1

)

select * from customers