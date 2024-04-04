from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import SecretStr


class Settings(BaseSettings):
    DATABASE_FILE: str
    # YADISK_ID: SecretStr
    # YADISK_SECRET: SecretStr
    # YADISK_TOKEN: SecretStr
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='UTF-8')


config = Settings()
