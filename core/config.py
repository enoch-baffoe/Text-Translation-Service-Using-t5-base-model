from pydantic import BaseSettings


class Settings(BaseSettings):
    title: str = "Text translation using the T5-base model"
    api_prefix: str = "/api/v1"
    version: str = "1.0.0"
    release_id: str = "1.0.0"


# initializing the settings
settings = Settings()
