"""Application configuration skeleton.

Real values (DB URLs, SendGrid keys, etc.) should be injected via
environment variables or Secret Manager in deployment environments.
"""

from functools import lru_cache

from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    environment: str = Field(default="local")
    api_prefix: str = Field(default="/api")

    # Placeholders for later tickets
    database_url: str = Field(default="postgresql+psycopg://user:pass@localhost:5432/org_health")
    sendgrid_api_key: str = Field(default="CHANGE_ME")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    return Settings()  # type: ignore[arg-type]
