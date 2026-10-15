{{ config(materialized='table') }}

SELECT 
    order_id,
    customer_id,
    UPPER(product_name) AS product_name,  -- Product name ko uppercase me convert karna
    amount,
    CAST(order_date AS DATE) AS order_date
FROM {{ source('my_pipeline', 'bronze_orders') }}
WHERE amount > 0  -- Negative ya invalid amounts ko filter out karna