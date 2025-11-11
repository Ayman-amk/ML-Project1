from zenml import pipeline
import mlflow

from src.areyouacat.core.mlflow_setup import setup_mlflow
from src.areyouacat.core.logging import get_logger

from src.steps.data.zen_load_curated import zen_load_curated
from src.steps.training.zen_train_tf import zen_train_tf
from src.steps.evaluation.zen_evaluate import zen_evaluate
from src.steps.registration.zen_register import zen_register

log = get_logger(__name__)

@pipeline
def zen_baseline_pipeline():
    # DATA
    ds_meta = zen_load_curated()
    # TRAIN
    model_uri, val_metrics = zen_train_tf(ds_meta)
    # EVAL
    test_metrics = zen_evaluate(model_uri, ds_meta)
    # REGISTER
    decision = zen_register(model_uri, test_metrics)
    return decision

def run():
    # Ensure MLflow points to your server (or file store) before running
    setup_mlflow("areyouacat-zen-baseline")
    result = zen_baseline_pipeline()  # <-- execute ONCE; returns PipelineRunResponse
    log.info("ZenML pipeline finished. Run ID: %s", result.id)
    print("ZenML pipeline finished. Run ID:", result.id)

