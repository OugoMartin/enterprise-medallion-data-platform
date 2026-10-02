# Enterprise Medallion Data Platform

A portfolio-grade data engineering project that demonstrates batch ingestion, data quality, medallion architecture, Snowflake warehousing, dbt transformations, automated testing, CI/CD, governance, and observability.

## Architecture

```text
Source CSV/API
     |
Python ingestion + validation
     |
AWS S3 landing
     |
Snowflake / Snowpipe
     |
BRONZE (raw)
     |
dbt transformations + tests
     |
SILVER (validated)
     |
dbt dimensional modeling
     |
GOLD (facts, dimensions, marts)
     |
Power BI / Tableau
```

## Engineering objectives

- Build traceable batch ingestion with source, batch, and ingestion metadata.
- Separate raw, validated, and business-ready data using Bronze/Silver/Gold layers.
- Enforce schema, null, duplicate, and business-rule checks.
- Model analytics-ready facts and dimensions with dbt.
- Automate Python and dbt validation through GitHub Actions.
- Document lineage, governance, security, deployment, and operational monitoring.
- Record only measured pipeline results; no performance claims are fabricated.

## Source data

The project is designed around the public dbt Labs Jaffle Shop sample domain: customers, orders, order items, products, stores, and supplies. Source data is intentionally not duplicated in this repository until its provenance and redistribution terms are documented.

## Repository layout

```text
src/                 Python ingestion and validation
sql/                 Snowflake DDL and layer SQL
dbt/                 dbt project models and tests
tests/               pytest unit tests
monitoring/          operational logging components
docs/                governance, quality, lineage, deployment docs
architecture/        architecture documentation/assets
screenshots/         evidence captured from actual project runs
.github/workflows/    CI automation
```

## Local setup

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
pytest
```

Copy `.env.example` to `.env` for local configuration. Never commit credentials.

## Planned implementation

1. Source profiling and validation
2. AWS S3 landing-zone ingestion
3. Snowflake Bronze ingestion
4. Silver cleaning and quality enforcement
5. Gold dimensional models and marts
6. dbt tests and documentation
7. GitHub Actions CI/CD
8. Pipeline observability
9. Power BI/Tableau consumption layer

## Status

Foundation implemented. Cloud resources, Snowflake objects, dbt models, measured execution results, and screenshots will be added as they are completed and validated.
