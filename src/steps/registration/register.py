import mlflow
from src.areyouacat.core.settings import SETTINGS
from src.areyouacat.core.logging import get_logger

log = get_logger(__name__)

def register_model(model_info, test_metrics):
    mlflow.log_param("promote_if_test_acc_ge", 0.60)
    decision = "skip"
    if test_metrics.get("test_accuracy", 0) >= 0.60:
        decision = "would_promote_to_Staging"

    mlflow.set_tag("model_name", SETTINGS.MODEL_NAME)
    mlflow.set_tag("registration_decision", decision)

    log.info(f"Registration step (placeholder): decision={decision}, model={SETTINGS.MODEL_NAME}")
    return {"decision": decision}
