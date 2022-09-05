from pydantic import BaseSettings


class Settings(BaseSettings):
    MONGO_CLUSTER: str
    DB_NAME: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
