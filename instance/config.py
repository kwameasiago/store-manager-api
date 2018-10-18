class Config:
	DEBUG=True
	ENV='development'
	TESTING=False

class TestConfig:
	TESTING = True


app_config = {
	'testing':TestConfig,
	'development':Config
}

