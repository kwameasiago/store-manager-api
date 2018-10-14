from flask import Flask


def create_app(blueprint1,cfg):
	app = Flask(__name__)
	app.register_blueprint(blueprint1)
	app.config.from_object(cfg)
	app.run()