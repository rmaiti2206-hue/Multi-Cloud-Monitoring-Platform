# Architecture

React.js provides the dashboard. FastAPI provides REST APIs and cloud-provider adapters. Prometheus collects metrics and Grafana visualizes time-series data. AWS, Azure and GCP are accessed only through authorized credentials/roles.

Flow:
User -> React -> FastAPI -> Cloud SDKs
                         -> Prometheus -> Grafana
                         -> Database
