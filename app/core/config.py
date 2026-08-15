from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import List
from urllib.parse import quote_plus

class Settings(BaseSettings):
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_SERVER: str = "db"
    POSTGRES_PORT: str = "5432"
    POSTGRES_DB: str
    SECRET_KEY: str = "dev-secret"
    JWT_SECRET: str = "dev-jwt-secret"
    ALGORITHM: str = "HS256"

    ALLOWED_ORIGINS: List[str] = []
    ALLOWED_HOSTS: List[str] = []
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60
    AUTH_PREFIX: str = 'Bearer '

    @property
    def DATABASE_URL(self):
        # encoded_password = quote_plus(self.POSTGRES_PASSWORD).replace("%", "%%")
        return f"postgresql://{self.POSTGRES_SERVER}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"
        
    
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )

settings = Settings()
