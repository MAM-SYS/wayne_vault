from pathlib import Path
from pathlib import PosixPath
from typing import Optional

from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')

    DEBUG: bool = False
    PROJECT_NAME: str = "wayne_vault"
    API_V1_STR: str = "/api/v1"
    BASE_DIR: PosixPath = Path(__file__).resolve().parent.parent.parent
    SITE_URL: str = "https://wayne_vault.tomanpay.com"
    SECRET_KEY: SecretStr
    LOGGING_CONFIG: str = 'logging.ini'

    DB_USER: str = None
    DB_PASSWORD: SecretStr = SecretStr("")
    DB_NAME: str = None
    DB_HOST: str = None
    DB_PORT: int = None
    DB_POOL_SIZE: int = 100
    DB_POOL_RECYCLE: int = 1800
    DB_POOL_PRE_PING: bool = True

    REDIS_HOST: str = "localhost"
    REDIS_PORT: int = 6377
    REDIS_PASSWORD: Optional[SecretStr] = None
    REDIS_DB: int = 0

    REDIS_MAX_CONNECTIONS: Optional[int] = None

    @property
    def SQLALCHEMY_DATABASE_URI(self):
        return f"mysql+aiomysql://" \
               f"{settings.DB_USER}:{settings.DB_PASSWORD.get_secret_value()}" \
               f"@{settings.DB_HOST}:{settings.DB_PORT}" \
               f"/{settings.DB_NAME}"

    @property
    def REDIS_URI(self):
        return f"redis:// \
        :{self.REDIS_PASSWORD.get_secret_value() if self.REDIS_PASSWORD else ''} \
        @{self.REDIS_HOST}:{self.REDIS_PORT} \
        /{self.REDIS_DB}"


settings = Settings(".env")
