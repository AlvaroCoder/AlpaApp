from pydantic_settings import BaseSettings
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent


class Settings(BaseSettings):
    app_name: str = "AgroRota"
    app_env: str = "development"
    secret_key: str = "change-me-in-production"
    database_url: str = "sqlite+aiosqlite:///./agrota.db"
    nominatim_user_agent: str = "agrota-app"

    model_dir: Path = BASE_DIR / "ml" / "models"
    upload_dir: Path = BASE_DIR.parent / "data" / "uploads"
    processed_dir: Path = BASE_DIR.parent / "data" / "processed"

    class Config:
        env_file = ".env"


settings = Settings()
