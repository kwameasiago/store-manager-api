from flask import request
from flask_restplus import Resource, Namespace,fields

from ..utils.auth import token_required
from ..model.users import Accounts

ns_users = Namespace('users',description='Users endpoints')
mod_login = ns_users.model('users model',{
	'email':fields.String('Users email'),
	'role': fields.String('Role of user'),
	'password':fields.String('Users password')
	})

mod_register = ns_users.model('register store attendant',{
	'first_name':fields.String('attendant\'s first name'),
	'last_name': fields.String('attendants\'s last name'),
	'email': fields.String('attendant\'s email'),
	'role': fields.String('attendant\'s role'),
	'password': fields.String('attendant\'s role')
	})

@ns_users.route('/login')
class Login(Resource):
	@ns_users.expect(mod_login)
	def post(self):
		obj = Accounts(request.get_json())
		if obj.check_user_input() == 1:
			return obj.login()
		else:
			return obj.check_user_input()


@ns_users.route('/register')
class RegisterAttendant(Resource):
	@token_required
	@ns_users.doc(security='apikey')
	@ns_users.expect(mod_register)
	def post(self):
		data = request.get_json()
		obj = Accounts(data)
		if obj.check_register_input() == 1:
			return Accounts.accounts
		else:
			return obj.check_register_input()