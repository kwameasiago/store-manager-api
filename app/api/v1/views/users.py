from flask import request
from flask_restplus import Resource, Namespace,fields


ns_users = Namespace('users',description='Users endpoints')
mod = ns_users.model('users model',{
	'email':fields.String('Users email'),
	'password':fields.String('Users password')
	})

@ns_users.route('/login')
class Login(Resource):
	def post(self):
		return {'testing': 'testing'}


@ns_users.route('/register/attendant')
class RegisterAttendant(Resource):
	def post(self):
		return {'testing': 'testing'}