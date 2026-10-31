# Omnichannel Retail Analytics Suite

## Overview
An end-to-end retail analytics project combining Python, SQL, machine learning, and Power BI to analyse product sales and outlet performance.

## Tools
- Python: Pandas, NumPy, Scikit-learn
- SQL: SQLite
- Visualization: Power BI
- Machine Learning: Random Forest Regression

## Dataset
The Big Mart Sales dataset contains 8,523 records and 12 original columns covering product attributes, outlet characteristics, and item outlet sales.

## Project Workflow
1. Cleaned missing values and standardized product categories.
2. Loaded the processed dataset into SQLite.
3. Used SQL to analyse sales by product category, outlet type, location tier, and price band.
4. Built an interactive Power BI dashboard with sales KPIs, charts, and slicers.
5. Trained a Random Forest regression model to predict item outlet sales.

## Key Findings
- Total recorded sales: 18.59 million.
- Fruits and Vegetables generated the highest sales among product categories.
- Supermarket Type 1 contributed the highest total sales among outlet types.
- Tier 3 outlets had the highest total sales among location tiers.

## Model Evaluation
A Random Forest model achieved:
- MAE: 718.78
- RMSE: 1,031.97
- R²: 0.6082

The model reduced MAE by approximately 45.6% compared with a mean-prediction baseline (MAE: 1,321.74).

## Limitations
The dataset does not contain a transaction date or historical time series. Therefore, this project predicts sales from product and outlet characteristics rather than forecasting future demand over time. Sales should not be interpreted as profit.

## Future Improvements
- Test alternative regression models and tune hyperparameters.
- Analyse feature importance and prediction errors.
- Add time-series forecasting when suitable dated sales data becomes available.
- Improve dashboard usability and document business recommendations.
