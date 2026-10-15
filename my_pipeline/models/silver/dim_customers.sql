{{ config(materialized='table') }}

SELECT DISTINCT
    customer_id,
    'Customer_' || customer_id AS customer_name  -- Ek dummy name generate karna
FROM {{ ref('silver_orders') }}