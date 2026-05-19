# HaYoung Log Platform Architecture

## 1. Project Overview

HaYoung Log Platform은 1000만 사용자 규모의 서비스에서 발생하는 대규모 사용자 행동 로그를 수집, 저장, 정제, 분석하기 위한 데이터 엔지니어링 포트폴리오 프로젝트입니다.

이 프로젝트는 단순히 로그를 저장하는 시스템이 아니라, 다음 흐름을 하나의 데이터 플랫폼으로 구현하는 것을 목표로 합니다.

```text

Log Generation
  → Event Ingestion
  → Stream Buffer
  → Raw Data Storage
  → Data Cleaning
  → Analytical Mart
  → Query & Dashboard