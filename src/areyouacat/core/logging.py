import logging
import sys
from typing import Optional
from .settings import SETTINGS

class _PlainFormatter(logging.Formatter):
    def format(self, record: logging.LogRecord) -> str:
        record.env = getattr(record, "env", SETTINGS.ENV)
        return super().format(record)

def _build_handler(level: str) -> logging.Handler:
    handler = logging.StreamHandler(sys.stdout)
    fmt = "%(asctime)s | %(levelname)s | %(env)s | %(name)s | %(message)s"
    datefmt = "%Y-%m-%d %H:%M:%S"
    handler.setFormatter(_PlainFormatter(fmt=fmt, datefmt=datefmt))
    handler.setLevel(level)
    return handler

def get_logger(name: Optional[str] = None) -> logging.Logger:
    """Project-wide logger with consistent formatting."""
    level = SETTINGS.LOG_LEVEL
    logger = logging.getLogger(name or "areyouacat")
    if not logger.handlers:
        logger.setLevel(level)
        logger.addHandler(_build_handler(level))
        logger.propagate = False
    return logger
