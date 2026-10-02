# Data Lineage

Current intended lineage:

```text
Source -> S3 landing -> Snowflake Bronze -> dbt Silver -> dbt Gold -> BI
```

Operational metadata includes source file, batch ID, and ingestion timestamp so records can be traced back to ingestion events. Detailed model-level lineage will be generated as dbt models are implemented.
