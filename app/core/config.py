from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    PROJECT_NAME: str = "Calculator"
    VERSION: str = "1.0.0"

    model_config = SettingsConfigDict(env_file=".env", case_sensitive=True)


settings = Settings()
