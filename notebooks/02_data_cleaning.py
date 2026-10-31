
import pandas as pd
from pathlib import Path

# Load raw data
df = pd.read_csv("data/big_mart_sales.csv")

print("Original shape:", df.shape)

# 1. Remove duplicate records
df = df.drop_duplicates()

# 2. Fill missing item weights using median weight per item
df["Item_Weight"] = df.groupby("Item_Identifier")[
    "Item_Weight"
].transform(lambda x: x.fillna(x.median()))

# Fill any remaining missing weights with overall median
df["Item_Weight"] = df["Item_Weight"].fillna(
    df["Item_Weight"].median()
)

# 3. Fill missing outlet sizes using the most common size
outlet_size_map = (
    df.dropna(subset=["Outlet_Size"])
    .groupby("Outlet_Identifier")["Outlet_Size"]
    .agg(lambda x: x.mode().iloc[0])
)

df["Outlet_Size"] = df["Outlet_Size"].fillna(
    df["Outlet_Identifier"].map(outlet_size_map)
)

# Fill any remaining outlet sizes with overall mode
df["Outlet_Size"] = df["Outlet_Size"].fillna(
    df["Outlet_Size"].mode()[0]
)

# 4. Standardize inconsistent fat-content labels
df["Item_Fat_Content"] = df["Item_Fat_Content"].replace({
    "LF": "Low Fat",
    "low fat": "Low Fat",
    "reg": "Regular"
})

# 5. Create useful business features
df["Outlet_Age"] = 2026 - df["Outlet_Establishment_Year"]

df["MRP_Band"] = pd.cut(
    df["Item_MRP"],
    bins=[0, 70, 140, 210, float("inf")],
    labels=["Low", "Medium", "High", "Premium"]
)

# 6. Save cleaned data
output_path = Path("data/cleaned_retail_sales.csv")
df.to_csv(output_path, index=False)

# 7. Validate
print("\nCleaned shape:", df.shape)
print("\nRemaining missing values:")
print(df.isnull().sum())
print("\nDuplicate rows:", df.duplicated().sum())
print("\nSaved to:", output_path)
