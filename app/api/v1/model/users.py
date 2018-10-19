import jwt

from .verify import Verification


class Accounts(Verification):
	accounts = [{'first_name': 'admin', 'last_name': 'admin', 
	'email': 'admin@gmail.com','password': '1234'}]
	logs = []
	def __init__(self,items):
		self.items = items

	def check_user_input(self):
		strings = [self.items['email'],self.items['role'],self.items['password']]
		payload=self.is_login_payload(self.items) 
		if payload is False:
			return {'result':'invalid payload'},406
		elif self.is_empty(strings) is True:
			return {'result': 'data set is empty'},406
		elif self.is_whitespace(strings) is True:
			return {'result': 'data set contains only white space'},406
		elif self.is_email(self.items['email']) is True:
			return {'result': 'invalid email'}, 406
		elif self.items['role'] != 'admin' and self.items['role'] != 'attendant':
			return {'result': 'invalid role'}, 406
		else:
			return 1

	def login(self):
		for account in Accounts.accounts:
			if account.get('email') != self.items['email'] or account.get('password') != self.items['password']:
				return {'result': 'invalid user name or password'}
		token = jwt.encode({'email':self.items['email'],'role':self.items['role']},'qazxswedc').decode('UTF-8')
		return {'result':token}
