import os

class Config():
    ENVIRONMENT: str = os.environ.get("API_ENVIRONMENT")


config: Config = Config()