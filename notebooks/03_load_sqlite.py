
import pandas as pd
import sqlite3

# Load cleaned dataset
df = pd.read_csv("data/cleaned_retail_sales.csv")

# Create SQLite database
connection = sqlite3.connect("data/retail_analytics.db")

# Load data into a SQL table
df.to_sql(
    "retail_sales",
    connection,
    if_exists="replace",
    index=False
)

# Verify the table
result = pd.read_sql_query(
    "SELECT COUNT(*) AS total_records FROM retail_sales",
    connection
)

print("Records loaded into SQLite:")
print(result)

connection.close()

print("\nDatabase created: data/retail_analytics.db")
