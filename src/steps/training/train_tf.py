import mlflow
from src.areyouacat.core.logging import get_logger

log = get_logger(__name__)

def train_tf(dataset_meta):
    mlflow.log_param("trainer", "placeholder")
    mlflow.log_param("optimizer", "adam")
    mlflow.log_param("batch_size", 32)
    mlflow.log_metric("val_accuracy", 0.60)

    model_info = {"model_uri": "s3://example-bucket/models/baseline/placeholder"}
    log.info(f"Training completed (placeholder). Model at: {model_info['model_uri']}")
    return model_info
