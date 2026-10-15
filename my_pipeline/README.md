# 🚀 Production-Grade Modern Medallion Data Engineering Pipeline

An end-to-end local data engineering pipeline built using **Python, DuckDB, and dbt (Data Build Tool)**, implementing the industry-standard **Medallion Architecture (Bronze -> Silver -> Gold)** and **Kimball Dimensional Modeling (Star Schema)**.

---

## 🏗️ Architecture & Tech Stack
* **Ingestion Layer:** Python (`Faker`, `Pandas`) simulating real-time e-commerce transactions.
* **Storage & Compute:** **DuckDB** (Blazing-fast, serverless analytical database engine).
* **Transformation & Modeling:** **dbt** for modular SQL transformations, dependency lineage tracking, and automated testing.
* **Orchestration:** Python-based master orchestration script (`run_pipeline.py`) automating end-to-end execution.

---

## 🔄 Pipeline Layers & Data Flow

1. **Bronze Layer (Raw):** 
   - Captures raw streaming data directly from the ingestion script into unstructured/semi-structured raw tables (`bronze_orders`).
2. **Silver Layer (Cleaned & Dimensional Modeling):** 
   - Cleaned, filtered, and casted data transformed into an enterprise **Star Schema**:
     - **Dimension Tables (`dim_customers`, `dim_products`):** Stores descriptive context about entities.
     - **Fact Table (`fct_orders`):** Stores core transactional metrics and foreign keys.
3. **Gold Layer (Aggregated Analytics):** 
   - Business-level aggregations (`gold_daily_sales`) built directly on top of the Fact table, ready for BI consumption (Metabase / Power BI).

---

## 🛡️ Data Quality & Testing
Automated testing integrated via dbt schema tests (`unique`, `not_null`) to enforce data integrity constraints and prevent bad data from reaching downstream analytics.

---

## 🚀 How to Run Locally

1. **Clone the repository & create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate