import pandas as pd
import awswrangler as wr

GLUE_DATABASE = "de-c1w2-analytics-db"

# Query 1: Total sales by country
total_sales_by_country = wr.athena.read_sql_query(
    """
    SELECT
        dim_locations.country,
        SUM(fact_orders.orderAmount) AS total_sales
    FROM fact_orders
    JOIN dim_locations
        ON fact_orders.postalCode = dim_locations.postalCode
    GROUP BY dim_locations.country
    ORDER BY total_sales DESC
    """,
    database=GLUE_DATABASE,
)

print(total_sales_by_country.head(10))


# Query 2: Product-level sales details
product_sales_details = wr.athena.read_sql_query(
    """
    SELECT
        fact_orders.orderDate,
        dim_products.productLine,
        dim_products.productName,
        dim_locations.country,
        SUM(fact_orders.orderAmount) AS total_sales
    FROM fact_orders
    JOIN dim_products
        ON fact_orders.productCode = dim_products.productCode
    JOIN dim_locations
        ON fact_orders.postalCode = dim_locations.postalCode
    GROUP BY
        fact_orders.orderDate,
        dim_products.productLine,
        dim_products.productName,
        dim_locations.country
    """,
    database=GLUE_DATABASE,
)

print(product_sales_details.head())
