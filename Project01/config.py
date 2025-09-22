from pydantic_settings import BaseSettings, SettingsConfigDict


class DataBaseConfiguration(BaseSettings):
  POSTGRES_PASSWORD:str
  POSTGRES_USERNAME:str
  POSTGRES_SERVER:str
  POSTGRES_PORT:int
  POSTGRES_DATABASE:str

  model_config = SettingsConfigDict(
    env_file="./.env",
    env_ignore_empty=True,
    extra="ignore"
  )


settings = DataBaseConfiguration() # type: ignore
