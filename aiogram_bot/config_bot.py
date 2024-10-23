"""Модуль конфига бота."""

from pydantic_settings import BaseSettings
from pydantic import SecretStr


class Settings(BaseSettings):
    """Загрузка секретов из .env"""

    bot_token: SecretStr
    database_url: str


config = Settings()
