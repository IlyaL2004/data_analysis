from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    POSTGRESQL_HOST: str
    POSTGRESQL_PORT: int
    POSTGRESQL_NAME: str
    POSTGRESQL_USER: str
    POSTGRESQL_PASS: str

    REDIS_HOST: str
    REDIS_PORT: int

    @property
    def DATABASE_URL_asyncpg(self):
        return f"postgresql+asyncpg://{self.POSTGRESQL_USER}:{self.POSTGRESQL_PASS}@{self.POSTGRESQL_HOST}:{self.POSTGRESQL_PORT}/{self.POSTGRESQL_NAME}"

    @property
    def REDIS_URL(self):
        return f"redis://{self.REDIS_HOST}:{self.REDIS_PORT}/0"  # 0 — это номер базы данных по умолчанию, можно расширить функционал, чтобы выбирать другую базу данных


    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()
