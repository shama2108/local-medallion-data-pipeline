{{ config(materialized='table') }}

SELECT DISTINCT
    product_name,
    CASE 
        WHEN product_name IN ('Laptop', 'Phone') THEN 'Electronics'
        ELSE 'Accessories'
    END AS product_category  -- Product ki category define karna
FROM {{ ref('silver_orders') }}