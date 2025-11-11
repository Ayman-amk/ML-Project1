# Architecture (Current)

-   **Core:** `src/areyouacat/core`
    -   `settings.py` – ENV/URI access
    -   `logging.py` – consistent JSON-like console logs
    -   `mlflow_setup.py` – tracking URI + experiment config
-   **Pipelines:**
    -   `baseline_pipeline.py` – pure-Python orchestration w/ nested MLflow runs
    -   `zen_baseline_pipeline.py` – ZenML @pipeline using steps in `src/steps/*`
-   **Steps:** (`src/steps`)
    -   `data/zen_load_curated.py` – returns dataset metadata (URIs/classes)
    -   `training/zen_train_tf.py` – logs placeholder training params/metrics
    -   `evaluation/zen_evaluate.py` – logs placeholder test metrics
    -   `registration/zen_register.py` – placeholder promotion decision

Next iterations will add:

-   Real data I/O (`tf.keras.utils.image_dataset_from_directory`)
-   Deepchecks data/model suites as gates
-   TF transfer learning (MobileNetV2)
-   MLflow Model Registry + Streamlit UI
