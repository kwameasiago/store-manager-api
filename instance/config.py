class Config:
	DEBUG=True
	ENV='development'

class TestConfig:
	DEBUG = False


app_config = {
	'testing':TestConfig,
	'development':Config
}

