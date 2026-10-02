# Architecture

The target architecture implements a medallion pattern with AWS S3 as the landing zone and Snowflake as the warehouse.

```text
CSV/API -> Python validation -> S3 landing -> Snowpipe -> Bronze -> dbt -> Silver -> dbt -> Gold -> BI
                                                   |                     |
                                                   +---- monitoring -----+
```

An exported architecture diagram will be added after the cloud resources are provisioned so the visual reflects the implemented system.
