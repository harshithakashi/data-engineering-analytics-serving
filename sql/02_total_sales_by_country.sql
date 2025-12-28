-- Total sales by country
SELECT
  dim_locations.country,
  SUM(fact_orders.orderAmount) AS total_sales
FROM fact_orders
JOIN dim_locations
  ON fact_orders.postalCode = dim_locations.postalCode
GROUP BY 1
ORDER BY total_sales DESC
LIMIT 10;
