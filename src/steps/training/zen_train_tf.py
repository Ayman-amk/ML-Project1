from zenml import step
import mlflow
from typing import Dict, Tuple
from src.areyouacat.core.logging import get_logger

log = get_logger(__name__)

@step
def zen_train_tf(dataset_meta: Dict) -> Tuple[str, Dict[str, float]]:
    """Placeholder trainer that logs a few params/metrics."""
    mlflow.log_param("trainer", "zen-placeholder")
    mlflow.log_param("optimizer", "adam")
    mlflow.log_param("batch_size", 32)
    mlflow.log_metric("val_accuracy", 0.60)

    model_uri = "s3://example-bucket/models/baseline/placeholder"
    log.info(f"Training completed (placeholder). Model at: {model_uri}")
    return model_uri, {"val_accuracy": 0.60}
