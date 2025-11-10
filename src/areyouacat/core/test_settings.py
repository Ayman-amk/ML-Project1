import sys, os
# --- Add project root to Python path ---
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../"))
if ROOT_DIR not in sys.path:
    sys.path.append(ROOT_DIR)

from src.areyouacat.core.settings import SETTINGS

if __name__ == "__main__":
    print("Environment:", SETTINGS.ENV)
    print("MLflow URI:", SETTINGS.MLFLOW_TRACKING_URI)
    print("Model name:", SETTINGS.MODEL_NAME)
