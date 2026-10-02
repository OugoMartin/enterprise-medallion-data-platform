# Dataset

The target business domain is based on the public dbt Labs Jaffle Shop example (customers, orders/items, products, stores, supplies). To keep CI self-contained and avoid redistributing third-party source data without context, `src/ingestion/generate_sample_data.py` creates deterministic synthetic transactional data for automated tests and demonstrations.

For the full upstream sample, retrieve it from the dbt Labs Jaffle Shop repository and preserve upstream attribution/licensing. Never describe synthetic records as production data.
