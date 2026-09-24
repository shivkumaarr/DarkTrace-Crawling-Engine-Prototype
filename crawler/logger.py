import logging
from pathlib import Path
from config import settings

Path(settings.LOG_FILE).parent.mkdir(parents=True, exist_ok=True)

logger = logging.getLogger("darktrace")
logger.setLevel(logging.INFO)

if not logger.handlers:
    handler = logging.FileHandler(settings.LOG_FILE, encoding="utf-8")
    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(message)s"
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    console = logging.StreamHandler()
    console.setFormatter(formatter)
    logger.addHandler(console)
