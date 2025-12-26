from pydantic import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Nutri-Trek API"
    debug: bool = True

    class Config:
        env_file = ".env"


settings = Settings()
