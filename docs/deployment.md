# Deployment

## Environments

The target lifecycle is DEV -> TEST -> PROD, with disaster-recovery considerations documented as the cloud implementation matures.

## CI

GitHub Actions runs unit tests for code changes. dbt compile/test gates will be added when the dbt project is connected to Snowflake. Cloud deployment is not enabled until credentials, environments, and rollback procedures are configured safely.
