
import snowflake.snowpark.functions as f
from snowflake.snowpark.functions import col

def model(dbt, session):
    dbt.config(
        materialized="table"
    )

    customers_df = dbt.ref("stg_customers_py")
    orders_df = dbt.ref("fct_orders")

    customer_orders_df = (
            orders_df
            .group_by(col("customer_id"))
            .agg([f.min(col("order_date")).alias("first_order"), f.max("order_date").alias("most_recent_order"), f.count("order_id").alias("number_of_orders"), f.sum("amount").alias("lifetime_value")])
        )
    
    final_df = (
        customers_df
        .join(customer_orders_df, customer_orders_df.customer_id == customers_df.customer_id, join_type="left")
        .drop(customer_orders_df.customer_id)
        .with_column_renamed(customers_df.customer_id, "customer_id")
    )
    return final_df 