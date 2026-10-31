
import sqlite3
from pathlib import Path
import pandas as pd

db_path = "data/retail_analytics.db"
output_dir = Path("reports")
output_dir.mkdir(exist_ok=True)

queries = {
    "overall_performance": """
        SELECT COUNT(*) AS total_records,
               ROUND(SUM(Item_Outlet_Sales), 2) AS total_sales,
               ROUND(AVG(Item_Outlet_Sales), 2) AS avg_sales_per_record
        FROM retail_sales;
    """,
    "outlet_performance": """
        SELECT Outlet_Type,
               ROUND(SUM(Item_Outlet_Sales), 2) AS total_sales,
               ROUND(AVG(Item_Outlet_Sales), 2) AS avg_sales
        FROM retail_sales
        GROUP BY Outlet_Type
        ORDER BY total_sales DESC;
    """,
    "category_performance": """
        SELECT Item_Type,
               ROUND(SUM(Item_Outlet_Sales), 2) AS total_sales
        FROM retail_sales
        GROUP BY Item_Type
        ORDER BY total_sales DESC;
    """,
    "location_performance": """
        SELECT Outlet_Location_Type,
               ROUND(SUM(Item_Outlet_Sales), 2) AS total_sales
        FROM retail_sales
        GROUP BY Outlet_Location_Type
        ORDER BY total_sales DESC;
    """,
    "price_band_performance": """
        SELECT MRP_Band,
               ROUND(AVG(Item_Outlet_Sales), 2) AS avg_sales
        FROM retail_sales
        GROUP BY MRP_Band
        ORDER BY avg_sales DESC;
    """
}

with sqlite3.connect(db_path) as conn:
    for name, query in queries.items():
        result = pd.read_sql_query(query, conn)
        result.to_csv(output_dir / f"{name}.csv", index=False)

        print(f"\n--- {name.upper()} ---")
        print(result.to_string(index=False))

print("\nSQL analysis complete. Results saved in reports/.")
