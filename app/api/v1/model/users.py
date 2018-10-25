import jwt
from flask import request

from .verify import Verification
accounts = [{'id':0,'first_name': 'admin', 'last_name': 'admin', 
	'email': 'admin@gmail.com','password': '1234'}]

class Accounts(Verification):
	"""
	class for user accounts
	"""
	def __init__(self,items):
		self.items = items

	def check_user_input(self):
		strings = [self.items['email'],self.items['password']]
		keys = ['email','password']
		payload=self.is_login_payload(self.items) 
		if payload is False:
			res = {'result':'invalid payload'},406
		elif self.is_empty(strings) is not False:
			res = {'result': 'data set {} is empty'.format(keys[self.is_empty(strings)])},406
		elif self.is_whitespace(strings) is not False:
			res = {'result': 'data set {} contains only white space'.format(keys[self.is_whitespace(strings)])},406
		elif self.is_email(self.items['email']) is True:
			res = {'result': 'invalid email'}, 406
		else:
			res = 1
		return res

	def login(self):
		for account in accounts:
			if account.get('email') == self.items['email']:
				token = jwt.encode({'id':account['id']},'qazxswedc',algorithm='HS256').decode('UTF-8')
				return [{'message': 'Login successful'},{'token':token}]
		return {'result': 'email or password invalid'},406


	def check_register_input(self):
		strings = [self.items['first_name'],self.items['last_name'],self.items['role'],
		self.items['email'],self.items['password']]
		keys = ['first name', 'last_name', 'role', 'email', 'password']
		payload = self.is_register_payload(self.items)
		if payload is False:
			return {'result':'invalid payload'},406
		elif self.is_whitespace(strings) is not False:
			return {'result': 'data set {} contains only white space'.format(keys[self.is_whitespace(strings)])},406
		elif self.is_empty(strings) is not False:
			return {'result': 'data set {} is empty'.format(keys[self.is_empty(strings)])}
		elif self.is_email(self.items['email']) is True:
			return {'result': 'invalid email'}, 406
		elif self.items['role'] != 'admin' and self.items['role'] != 'attendant':
			return {'result': 'invalid role'}, 406
		else:
			self.items['id'] = len(accounts)
			accounts.append(self.items)
			return 1

	@classmethod
	def get_id(cls):
		token = request.headers['X-API-KEY']
		userId = token = jwt.decode(token,'qazxswedc',algorithms=['HS256']),401
		return userId
