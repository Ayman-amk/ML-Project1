from zenml import step
import mlflow
from typing import Dict
from src.areyouacat.core.settings import SETTINGS
from src.areyouacat.core.logging import get_logger

log = get_logger(__name__)

@step
def zen_register(model_uri: str, test_metrics: Dict[str, float]) -> Dict[str, str]:
    """Placeholder registry decision."""
    threshold = 0.60
    mlflow.log_param("promote_if_test_acc_ge", threshold)
    decision = "would_promote_to_Staging" if test_metrics.get("test_accuracy", 0) >= threshold else "skip"

    mlflow.set_tag("model_name", SETTINGS.MODEL_NAME)
    mlflow.set_tag("registration_decision", decision)
    log.info(f"Registration step: decision={decision}, model={SETTINGS.MODEL_NAME}")
    return {"decision": decision}
