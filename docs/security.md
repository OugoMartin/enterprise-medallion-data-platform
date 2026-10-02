# Security and Access Management

## Principles

- No credentials are stored in source control.
- Local configuration uses environment variables.
- AWS access should use profiles or IAM roles where possible.
- Snowflake access will follow least privilege and role-based access control (RBAC).
- Sensitive columns introduced in later datasets will use masking policies where appropriate.

## Planned Snowflake roles

- DATA_ENGINEER
- DATA_ANALYST
- DATA_SCIENTIST

Grants and masking-policy SQL will be added only after the warehouse objects are implemented and tested.
