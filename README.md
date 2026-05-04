# HaYoung

**HaYoung**은 제주도 사투리로 “많다”, “많이”라는 뜻을 가진 단어입니다.  
이 프로젝트는 많은 데이터를 안정적으로 수집하고, 처리하고, 가공하여 비즈니스 의사결정에 도움이 되는 결과를 제공한다는 의미를 담고 있습니다.

## Overview

HaYoung은 커머스 서비스에서 발생하는 주문, 상품, 사용자 행동 로그를 수집하고 분석 가능한 형태로 정제하여 비즈니스 지표로 제공하는 End-to-End 데이터 플랫폼 프로젝트입니다.

이 프로젝트는 Python 기반 데이터 생성기, Kafka 이벤트 수집, Spark Batch 처리, PostgreSQL Warehouse, dbt 데이터 모델링, Airflow 워크플로우 오케스트레이션, Metabase BI 대시보드로 구성됩니다.

## MVP Goals

- 샘플 커머스 데이터 생성
- Kafka 또는 Redpanda 기반 이벤트 적재
- Spark Batch 기반 데이터 정제
- PostgreSQL Warehouse 적재
- dbt 기반 mart 모델링
- Airflow DAG 기반 파이프라인 실행
- Metabase 기반 BI 대시보드 구성

## Architecture

```text
Data Generator
  → Kafka / Redpanda
  → Spark Batch
  → PostgreSQL Warehouse
  → dbt Models
  → Metabase Dashboard

Airflow
  → Orchestrates the whole pipeline
```

## Tech Stack

- Python
- uv
- Docker Compose
- Kafka / Redpanda
- Spark
- PostgreSQL
- dbt
- Airflow
- Metabase

## Project Structure

```text
HaYoung/
  data-generator/
  spark/
  airflow/
  dbt/
  metabase/
  docs/
```

## Project Purpose

이 프로젝트의 목적은 단순한 ETL 구현이 아니라, 경영진·상품팀·마케팅팀이 공통된 기준으로 매출, 상품 성과, 전환율을 확인할 수 있는 데이터 제품을 만드는 것입니다.
