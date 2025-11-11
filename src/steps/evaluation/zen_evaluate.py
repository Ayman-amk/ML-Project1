from zenml import step
import mlflow
from typing import Dict
from src.areyouacat.core.logging import get_logger

log = get_logger(__name__)

@step
def zen_evaluate(model_uri: str, dataset_meta: Dict) -> Dict[str, float]:
    """Placeholder evaluator."""
    metrics = {"test_accuracy": 0.58}
    for k, v in metrics.items():
        mlflow.log_metric(k, v)
    log.info(f"Evaluation done (placeholder). Metrics: {metrics}")
    return metrics
