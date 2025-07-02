import os
from loguru import logger
from app.core.config import settings

# Remove default logger
logger.remove()

# Configure logger
logger.add(
    "edurag.log",
    rotation="500 MB",
    retention="7 days",
    level=settings.LOG_LEVEL,
    compression="zip"
)

# Console logging if needed
logger.add(
    lambda msg: print(msg, end=''),
    level=settings.LOG_LEVEL,
    colorize=True,
    format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level}</level> | {message}"
)

def get_logger(name: str = None):
    if name:
        return logger.bind(name=name)
    return logger