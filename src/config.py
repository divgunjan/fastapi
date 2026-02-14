from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import load_dotenv
import os

class Settings(BaseSettings):
    DATABASE_URL:str | None=None
    JWT_SECRET:str | None=None
    JWT_ALGORITHM:str| None=None
    REDIS_HOST:str
    REDIS_PORT:int
    model_config = SettingsConfigDict(
        env_file=".env",
        extra = "ignore"
    )

Config = Settings(DATABASE_URL="postgresql+asyncpg://postgres:Postgres2025@localhost:5432/bookly_db",JWT_SECRET=os.getenv("JWT_SECRET"), JWT_ALGORITHM=os.getenv("JWT_ALGORITHM"),REDIS_HOST="localhost",REDIS_PORT=6379)
