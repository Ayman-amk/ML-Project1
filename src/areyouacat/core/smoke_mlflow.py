from .mlflow_setup import setup_mlflow
from .logging import get_logger
import mlflow

log = get_logger(__name__)

if __name__ == "__main__":
    setup_mlflow("areyouacat-demo")

    with mlflow.start_run(run_name="smoke_run"):
        mlflow.log_param("hello", "world")
        mlflow.log_metric("accuracy", 0.95)
        log.info("Logged a smoke run to MLflow.")
        print("Run complete. If you have MLflow UI running at http://127.0.0.1:5000,")
        print("you'll find experiment 'areyouacat-demo' with run 'smoke_run'.")
