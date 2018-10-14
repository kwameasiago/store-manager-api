from app import create_app
from app.api.v1 import app_v1
from instance.config import Config

create_app(app_v1,Config)