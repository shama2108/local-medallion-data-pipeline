{{ config(materialized='table') }}

SELECT 
    order_date,
    COUNT(order_id) AS total_orders,
    SUM(amount) AS total_revenue,
    ROUND(AVG(amount), 2) AS average_order_value
FROM {{ ref('fct_orders') }}
GROUP BY order_date
ORDER BY order_date DESC