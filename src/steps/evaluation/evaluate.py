import mlflow
from src.areyouacat.core.logging import get_logger

log = get_logger(__name__)

def evaluate(model_info, dataset_meta):
    metrics = {"test_accuracy": 0.58}
    for k, v in metrics.items():
        mlflow.log_metric(k, v)
    log.info(f"Evaluation completed (placeholder). Metrics: {metrics}")
    return metrics
