![Python](https://img.shields.io/badge/python-3.10+-blue)
![MLflow](https://img.shields.io/badge/MLflow-2.14-success)
![ZenML](https://img.shields.io/badge/ZenML-0.91-informational)

# 🐾 Machine Project 1 — Are You A Cat?

An end-to-end **MLOps image classification system** demonstrating a complete, production-style lifecycle — from data ingestion and model training to tracking, validation, and deployment.

---

## 🧠 Tech Stack

| Phase                              | Technology              | Purpose                                 |
| ---------------------------------- | ----------------------- | --------------------------------------- |
| **Modeling**                       | TensorFlow (CNN)        | Image classification backbone           |
| **Orchestration**                  | ZenML                   | Reproducible ML pipelines               |
| **Experiment Tracking & Registry** | MLflow (SQLite backend) | Logs metrics, parameters, and artifacts |
| **Validation**                     | Deepchecks _(up next)_  | Data and model integrity checks         |
| **Serving**                        | Streamlit _(up next)_   | Simple prediction UI                    |
| **Storage**                        | Local / S3 _(future)_   | Artifact & feedback storage             |

---

## 🎯 Goal

Predict whether an image shows a **cat** —
but more importantly, showcase a **reproducible, modular, and production-ready MLOps pipeline** using modern open-source tools.

---

## 📂 Project Structure

```
src/
└── areyouacat/
    ├── core/                  → settings, logging, mlflow setup
    ├── pipelines/
    │   ├── baseline_pipeline.py       # Pure Python pipeline
    │   ├── zen_baseline_pipeline.py   # ZenML @pipeline implementation
    │   └── run_zen_baseline.py        # Runner entrypoint
    ├── steps/
    │   ├── data/           → zen_load_curated
    │   ├── training/       → zen_train_tf
    │   ├── evaluation/     → zen_evaluate
    │   └── registration/   → zen_register
    ├── configs/
    ├── docs/
    ├── infra/
    └── tests/
```

---

## ⚙️ Getting Started

### 1. Environment Setup

```bash
pip install mlflow zenml
zenml init
```

### 2. Start MLflow UI

Use SQLite to avoid deprecation warnings:

```bash
mlflow server --host 127.0.0.1 --port 5000   --backend-store-uri sqlite:///mlflow.db   --default-artifact-root ./mlruns
```

Then open **[http://127.0.0.1:5000](http://127.0.0.1:5000)** in your browser.

### 3. Run the ZenML Pipeline

```bash
python -m src.pipelines.run_zen_baseline
```

You’ll see logs for each step (`data → train → eval → register`)
and a new experiment named **`areyouacat-zen-baseline`** in MLflow.

> 💡 _If ZenML shows “Daemon functionality is not supported on Windows”, you can safely ignore it — everything still runs fine._

---

## 🧩 Current Progress

✅ Clean project scaffold
✅ Logging & settings modules
✅ MLflow setup with working UI
✅ Baseline ZenML pipeline (with placeholders)
🕓 Next: Real data loader + Deepchecks validation
🕓 Next: TensorFlow training + MLflow autolog
🕓 Next: Streamlit serving interface

---

## 🧱 Roadmap

-   [x] Base folder & environment setup
-   [x] Logging utilities
-   [x] ZenML baseline pipeline
-   [x] MLflow integration
-   [ ] Data ingestion + validation (Deepchecks)
-   [ ] Real TensorFlow CNN training
-   [ ] Model registry + evaluation artifacts
-   [ ] Streamlit UI + feedback loop
-   [ ] CI/CD workflow integration

---

## 🧰 Useful Commands

Run from the **repo root**:

```bash
python -m src.pipelines.run_zen_baseline
```

Clear ZenML cache:

```bash
zenml clean --yes
```

View ZenML dashboard locally:

```bash
zenml login --local
```

---

## 🧭 License

**MIT License** — free to use, modify, and share.

---

### ✨ Author

**Ayman Amokrane**
