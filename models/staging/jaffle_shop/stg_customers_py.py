def model(dbt, session):

    source_df = dbt.source("jaffle_shop", "customers")

    renamed_df = source_df.with_column_renamed(source_df.id, "customer_id")
    final_df = renamed_df.drop_duplicates() # stuff you can't write in SQL!
    
    return final_df