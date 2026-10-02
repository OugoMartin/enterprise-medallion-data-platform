CREATE TABLE IF NOT EXISTS ENTERPRISE_MEDALLION_DB.MONITORING.PIPELINE_RUNS (
    run_id VARCHAR NOT NULL,
    pipeline_name VARCHAR NOT NULL,
    batch_id VARCHAR,
    source_file VARCHAR,
    start_time TIMESTAMP_TZ,
    end_time TIMESTAMP_TZ,
    records_received NUMBER,
    records_loaded NUMBER,
    records_rejected NUMBER,
    status VARCHAR,
    error_message VARCHAR,
    duration_seconds NUMBER(18, 3),
    created_at TIMESTAMP_TZ DEFAULT CURRENT_TIMESTAMP()
);
