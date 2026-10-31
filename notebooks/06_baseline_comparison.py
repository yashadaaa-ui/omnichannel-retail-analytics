
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.dummy import DummyRegressor
from sklearn.metrics import mean_absolute_error, r2_score

df = pd.read_csv("data/cleaned_retail_sales.csv")

X = df.drop(columns=["Item_Outlet_Sales", "MRP_Band"])
y = df["Item_Outlet_Sales"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

baseline = DummyRegressor(strategy="mean")
baseline.fit(X_train, y_train)

predictions = baseline.predict(X_test)

print("BASELINE MODEL")
print(f"MAE: {mean_absolute_error(y_test, predictions):.2f}")
print(f"R2:  {r2_score(y_test, predictions):.4f}")
