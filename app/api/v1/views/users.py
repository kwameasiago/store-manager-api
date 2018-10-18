from flask import request
from flask_restplus import Resource, Namespace,fields

from ..utils.auth import login_required

ns_users = Namespace('users',description='Users endpoints')
mod = ns_users.model('users model',{
	'email':fields.String('Users email'),
	'role': fields.String('Role of user'),
	'password':fields.String('Users password')
	})

@ns_users.route('/login')
class Login(Resource):
	@ns_users.expect(mod)
	def post(self):
		return {'testing': 'testing'}


@ns_users.route('/register/attendant')
class RegisterAttendant(Resource):
	def post(self):
		return {'testing': 'testing'}