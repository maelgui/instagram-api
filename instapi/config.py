from pydantic import BaseSettings


class Settings(BaseSettings):
    instagram_app_id: str
    instagram_app_secret: str
    secret_key: str
    base_url: str

settings = Settings()
