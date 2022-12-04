def model(dbt, session):

    orders = dbt.ref("stg_orders")

    describe_df = orders.describe()

    return describe_df
    