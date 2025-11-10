# Machine Project 1 - Are You A Cat?

An end-to-end **MLOps image classification project** demonstrating a complete lifecycle:

-   **Model:** TensorFlow (CNN)
-   **Pipelines:** ZenML
-   **Tracking & Registry:** MLflow
-   **Validation:** Deepchecks
-   **Serving:** Streamlit
-   **Storage:** S3 (or MinIO local)

## Goal

Predict whether an image shows a cat — but more importantly, showcase a _reproducible, production-ready_ MLOps pipeline.

## Current Structure

-   **src/mlproject/** – Core logic, model, and utilities
-   **steps/** – ZenML step modules
-   **pipelines/** – ZenML pipeline definitions
-   **app/** – Streamlit or FastAPI interface
-   **infra/** – Docker & infrastructure setup
-   **configs/** – Environment configs
-   **tests/** – Unit & integration tests
-   **.github/** – CI/CD automation

## How to Start

1. Create a virtual environment
2. Add dependencies gradually as you use them
3. Run local tests and pipelines
4. Document everything in `/docs`

## Roadmap

-   [x] Base folder & settings
-   [ ] Logging utilities
-   [ ] Data pipeline
-   [ ] TensorFlow training
-   [ ] MLflow integration
-   [ ] Deepchecks validation
-   [ ] Streamlit UI + feedback loop
