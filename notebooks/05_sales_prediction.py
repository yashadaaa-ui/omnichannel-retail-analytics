
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Load cleaned data
df = pd.read_csv("data/cleaned_retail_sales.csv")

# Features and target
X = df.drop(columns=["Item_Outlet_Sales", "MRP_Band"])
y = df["Item_Outlet_Sales"]

# Identify column types
categorical_cols = X.select_dtypes(include="object").columns.tolist()
numerical_cols = X.select_dtypes(include=np.number).columns.tolist()

# Preprocessing
preprocessor = ColumnTransformer([
    ("numeric", SimpleImputer(strategy="median"), numerical_cols),
    ("categorical", Pipeline([
        ("imputer", SimpleImputer(strategy="most_frequent")),
        ("encoder", OneHotEncoder(handle_unknown="ignore"))
    ]), categorical_cols)
])

# Model pipeline
model = Pipeline([
    ("preprocessing", preprocessor),
    ("regressor", RandomForestRegressor(
        n_estimators=100,
        max_depth=12,
        min_samples_leaf=3,
        random_state=42,
        n_jobs=-1
    ))
])

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train and evaluate
model.fit(X_train, y_train)
predictions = model.predict(X_test)

mae = mean_absolute_error(y_test, predictions)
rmse = np.sqrt(mean_squared_error(y_test, predictions))
r2 = r2_score(y_test, predictions)

print(f"Training records: {len(X_train)}")
print(f"Testing records: {len(X_test)}")
print(f"MAE:  {mae:.2f}")
print(f"RMSE: {rmse:.2f}")
print(f"R²:   {r2:.4f}")

# Save test predictions for analysis
results = X_test.copy()
results["Actual_Sales"] = y_test
results["Predicted_Sales"] = predictions
results.to_csv("reports/sales_predictions.csv", index=False)

print("\nPredictions saved to reports/sales_predictions.csv")
