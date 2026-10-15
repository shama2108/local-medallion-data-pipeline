import duckdb
import pandas as pd
from faker import Faker
import random

fake = Faker()
data = []
for i in range(100):
    data.append({
        "order_id": 1000 + i,
        "customer_id": random.randint(1, 20),
        "product_name": random.choice(["Laptop", "Phone", "Headphones", "Keyboard", "Mouse"]),
        "amount": round(random.uniform(20.0, 1200.0), 2),
        "order_date": fake.date_between(start_date="-30d", end_date="today").isoformat()
    })

df = pd.DataFrame(data)

# Connect to DuckDB (creates 'analytics.duckdb' file automatically)
conn = duckdb.connect("analytics.duckdb")
conn.execute("CREATE TABLE IF NOT EXISTS bronze_orders AS SELECT * FROM df")
print("Bronze data loaded successfully into DuckDB!")
conn.close()