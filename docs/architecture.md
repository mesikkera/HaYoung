# Architecture

HaYoung의 MVP 아키텍처는 다음 흐름으로 구성됩니다.

```text
Data Generator
  → Kafka / Redpanda
  → Spark Batch
  → PostgreSQL Warehouse
  → dbt Models
  → Metabase Dashboard
