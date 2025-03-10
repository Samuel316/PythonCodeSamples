# MYSQL

duckdb.sql(f"SELECT * FROM mysql_query('DatabaseName', \"{mysql_request}\")").to_df()

# Prevents typing issues
duckdb.sql(f"CREATE OR REPLACE TABLE temp_table AS SELECT * FROM mysql_query('DatabaseName', \"{mysql_request}\")")
duckdb.sql("SELECT * FROM temp_table").to_df()


