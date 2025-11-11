import mlflow
from src.areyouacat.core.mlflow_setup import setup_mlflow
from src.areyouacat.core.logging import get_logger
from src.steps.data.load_curated import load_curated
from src.steps.training.train_tf import train_tf
from src.steps.evaluation.evaluate import evaluate
from src.steps.registration.register import register_model

log = get_logger(__name__)

def run():
    setup_mlflow("areyouacat-baseline")

    with mlflow.start_run(run_name="orchestrator") as parent_run:
        # DATA
        with mlflow.start_run(run_name="load_curated", nested=True):
            dataset_meta = load_curated()
            mlflow.log_param("classes", ",".join(dataset_meta["classes"]))
            mlflow.log_param("train_uri", dataset_meta["train_uri"])
            mlflow.log_param("val_uri", dataset_meta["val_uri"])
            mlflow.log_param("test_uri", dataset_meta["test_uri"])

        # TRAIN
        with mlflow.start_run(run_name="train", nested=True):
            model_info = train_tf(dataset_meta)

        # EVALUATE
        with mlflow.start_run(run_name="evaluate", nested=True):
            test_metrics = evaluate(model_info, dataset_meta)

        # REGISTER
        with mlflow.start_run(run_name="register", nested=True):
            decision_info = register_model(model_info, test_metrics)

        log.info(
            "Pipeline finished. Parent run_id=%s | decision=%s",
            parent_run.info.run_id,
            decision_info["decision"],
        )
        print(f"Done. Open MLflow and inspect run: {parent_run.info.run_id}")

if __name__ == "__main__":
    run()
