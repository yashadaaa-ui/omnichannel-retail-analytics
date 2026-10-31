
-- 1. Overall business performance
SELECT
    COUNT(*) AS total_records,
    ROUND(SUM(Item_Outlet_Sales), 2) AS total_sales,
    ROUND(AVG(Item_Outlet_Sales), 2) AS avg_sales_per_record
FROM retail_sales;

-- 2. Sales by outlet type
SELECT
    Outlet_Type,
    ROUND(SUM(Item_Outlet_Sales), 2) AS total_sales,
    ROUND(AVG(Item_Outlet_Sales), 2) AS avg_sales_per_record
FROM retail_sales
GROUP BY Outlet_Type
ORDER BY total_sales DESC;

-- 3. Sales by product category
SELECT
    Item_Type,
    ROUND(SUM(Item_Outlet_Sales), 2) AS total_sales
FROM retail_sales
GROUP BY Item_Type
ORDER BY total_sales DESC;

-- 4. Sales by location tier
SELECT
    Outlet_Location_Type,
    ROUND(SUM(Item_Outlet_Sales), 2) AS total_sales
FROM retail_sales
GROUP BY Outlet_Location_Type
ORDER BY total_sales DESC;

-- 5. Average sales by price band
SELECT
    MRP_Band,
    ROUND(AVG(Item_Outlet_Sales), 2) AS avg_sales
FROM retail_sales
GROUP BY MRP_Band
ORDER BY avg_sales DESC;
