from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    ENV: str = "dev"
    LOG_LEVEL: str = "INFO"

    AWS_ACCESS_KEY_ID: str | None = None
    AWS_SECRET_ACCESS_KEY: str | None = None
    AWS_DEFAULT_REGION: str = "us-east-1"
    S3_BUCKET: str = "areyouacat"

    MLFLOW_TRACKING_URI: str = "http://127.0.0.1:5000"

    MODEL_NAME: str = "are-you-a-cat"
    MODEL_STAGE: str = "Production"

    class Config:
        env_file = ".env"
        extra = "ignore"


@lru_cache
def get_settings() -> Settings:
    """Load and cache settings from .env."""
    return Settings()


SETTINGS = get_settings()
