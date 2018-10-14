from flask import Flask

from .api.v1 import app_v1


def create_app():
	app = Flask(__name__)
	app.register_blueprint(app_v1)
	app.config.from_envvar('config')
	return app