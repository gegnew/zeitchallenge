import logging
from functools import lru_cache
from logging.config import dictConfig

from app.config.settings import build_settings_object


# # @lru_cache
# def get_logger(logger_name: str = "lq") -> logging.Logger:
#     dictConfig(LogConfig().dict())
#     logger = logging.getLogger(logger_name)
#     return logger


# LOGGER = get_logger()
app_settings = build_settings_object()
# client = app_settings.db_client
