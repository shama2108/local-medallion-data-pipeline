{{ config(materialized='table') }}

SELECT 
    order_id,
    customer_id,
    product_name,
    amount,
    CAST(order_date AS DATE) AS order_date
FROM {{ ref('silver_orders') }}