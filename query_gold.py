import duckdb

# Connect to the DuckDB database file
conn = duckdb.connect("analytics.duckdb")  


print("--- Daily Sales Summary (Gold Layer) ---")
df = conn.execute("SELECT * FROM gold_daily_sales").fetchdf()

print(df)
conn.close()