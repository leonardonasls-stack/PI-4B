import os
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    PROJECT_NAME: str = "Vacina Alagoas"
    VERSION: str = "1.0.0"
    API_V1_STR: str = "/api/v1"

    # Credenciais do Banco PostgreSQL
    POSTGRES_USER: str | None = None
    POSTGRES_PASSWORD: str | None = None
    POSTGRES_DB: str | None = None

    DATABASE_URL: str
    SYNC_DATABASE_URL: str | None = None

    # Autenticação JWT
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 120

    ADMIN_USERNAME: str | None = None
    ADMIN_PASSWORD: str | None = None

    model_config = SettingsConfigDict(
        env_file=os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))), ".env"),
        env_file_encoding="utf-8",
        extra="ignore"
    )


settings = Settings()

