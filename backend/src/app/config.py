from pydantic_settings import BaseSettings
import os

class Settings(BaseSettings):
    PROJECT_NAME: str = "Vacina Alagoas"
    VERSION: str = "1.0.0"
    API_V1_STR: str = "/api/v1"
    
    # Credenciais do Banco PostgreSQL
    POSTGRES_USER: str = "postgres"
    POSTGRES_PASSWORD: str = "postgres"
    POSTGRES_DB: str = "vacinacao_al"
    
    DATABASE_URL: str = "postgresql+asyncpg://postgres:postgres@localhost:5432/vacinacao_al"
    SYNC_DATABASE_URL: str = "postgresql://postgres:postgres@localhost:5432/vacinacao_al"
    
    # Autenticação JWT
    SECRET_KEY: str = "superchavejwtseguraprojetointegrador2026"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 120
    
    ADMIN_USERNAME: str = "admin"
    ADMIN_PASSWORD: str = "admin123"

    class Config:
        env_file = ".env"
        extra = "allow"

settings = Settings()
