from typing import List

from pydantic import BaseSettings

from app.config.errors import Errors


class Settings(BaseSettings):
    class Config:
        env_file = ".env"
        case_sensitive = True

    PROJECT_NAME = "Zeit Challenge"
    API_VERSION: str = "/api/v1"

    INSTALLED_APPS = []

    BACKEND_CORS_ORIGINS: List[str] = []  # JSON-formatted
    FASTAPI_SECRET_KEY: str
    FASTAPI_HASH_ALGORITHM: str
    FASTAPI_ACCESS_TOKEN_EXPIRE_MINUTES: int

    @property
    def errors(self) -> Errors:
        return Errors()


def build_settings_object(**overrides):
    return Settings(**overrides)  # type: ignore


settings = Settings()
