{{ log("target: " ~ target,info=True) }}

with orders as (

    SELECT
        id as order_id,
        user_id as customer_id,
        order_date,
        status
    FROM {{ source('jaffle_shop', 'orders') }}

)

select * from orders