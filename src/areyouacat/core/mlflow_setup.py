"""
MLflow setup helper — configure tracking URI, experiment, and provide a client.
"""

import mlflow
from mlflow.tracking import MlflowClient
from .settings import SETTINGS
from .logging import get_logger

log = get_logger(__name__)

def setup_mlflow(experiment_name: str = "areyouacat") -> None:
    """Configure MLflow tracking URI and set experiment."""
    try:
        mlflow.set_tracking_uri(SETTINGS.MLFLOW_TRACKING_URI)
        mlflow.set_experiment(experiment_name)
        log.info(
            f"MLflow initialized (URI={SETTINGS.MLFLOW_TRACKING_URI}, "
            f"experiment={experiment_name})"
        )
    except Exception as e:
        log.error(f"Failed to setup MLflow: {e}")

def get_mlflow_client() -> MlflowClient | None:
    """Return an MLflow client (None if creation fails)."""
    try:
        return MlflowClient(tracking_uri=SETTINGS.MLFLOW_TRACKING_URI)
    except Exception as e:
        log.error(f"Failed to create MLflow client: {e}")
        return None
