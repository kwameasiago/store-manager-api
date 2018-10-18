import jwt

from functools import wraps
from flask import request
from ....app import create_app


def login_required(f):
	@wraps(f)
	def decorated(*arg,**kwargs):
		token = None
		if 'X-API-KEY' in request.headers:
			token = request.headers['X-API-KEY']
		if not token:
			return {'result': 'token is missing'}
		try:
			token = jwt.decode(token,app.config['SECRET_KEY'])
		except:
			return {'result': 'token is invalid'}
		return f(*arg,**kwargs)
	return decorated
