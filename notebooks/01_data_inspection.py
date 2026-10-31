
import pandas as pd
from pathlib import Path

# Load the dataset
file_path = Path("data/big_mart_sales.csv")
df = pd.read_csv(file_path)

# Basic inspection
print("Dataset shape:", df.shape)

print("\nColumn names:")
print(df.columns.tolist())

print("\nFirst 5 rows:")
print(df.head())

print("\nMissing values:")
print(df.isnull().sum())

print("\nData types:")
print(df.dtypes)
