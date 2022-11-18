from fastapi.templating import Jinja2Templates
from pydantic import BaseSettings
import os


APP_DIR = "app"
TEMPLATES_DIR = os.path.join(APP_DIR, "templates")

TEMPLATES = Jinja2Templates(directory=TEMPLATES_DIR)


class Environment(BaseSettings):
    API_KEY: str

    class Config:
        env_prefix = ""
        case_sensitive = False
        env_file = ".env"
        env_file_encoding = "utf-8"


ENV = Environment()
