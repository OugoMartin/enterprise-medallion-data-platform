# Data Quality Framework

The project validates data before promotion across medallion layers.

## Initial controls

- Required-column/schema validation
- Null profiling
- Duplicate detection
- Source row counts
- Batch and source-file traceability

## Planned controls

Silver-layer rules will add type, domain, referential-integrity, uniqueness, and business-rule validation. Invalid records will be isolated rather than silently discarded. dbt tests will provide warehouse-level validation.

## Evidence policy

Quality rates and failure counts are recorded only from actual pipeline executions. The repository does not use invented success rates.
