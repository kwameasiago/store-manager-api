class Config:
	SECRET_KEY = 'qazxswedc'
	DEBUG=False
	ENV='development'
	TESTING=False

class TestConfig(Config):
	TESTING = True

class DevelopmentConfig(Config):
	DEBUG = True

app_config = {
	'testing':TestConfig,
	'development':DevelopmentConfig
}

