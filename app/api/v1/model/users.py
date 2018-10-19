import jwt

from .verify import Verification


class Accounts(Verification):
	"""
	class for user accounts
	"""
	accounts = [{'first_name': 'admin', 'last_name': 'admin', 
	'email': 'admin@gmail.com','password': '1234'}]
	def __init__(self,items):
		self.items = items
		self.role = self.items['role'] != 'admin' and self.items['role'] != 'attendant'

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
		elif self.role:
			return {'result': 'invalid role'}, 406
		else:
			return 1

	def login(self):
		token = jwt.encode({'email':self.items['email'],'role':self.items['role']},'qazxswedc',
			algorithm='HS256').decode('UTF-8')
		for account in Accounts.accounts:
			if account.get('email') == self.items['email']:
				return {'result':token}
		return {'result': 'email or password invalid'},406

	def check_register_input(self):
		strings = [self.items['first_name'],self.items['last_name'],self.items['role'],
		self.items['email'],self.items['password']]
		payload = self.is_register_payload(self.items)
		if payload is False:
			return {'result':'invalid payload'},406
		elif self.is_whitespace(strings) is True:
			return {'result': 'data set contains only white space'},406
		elif self.is_email(self.items['email']) is True:
			return {'result': 'invalid email'}, 406
		elif self.role:
			return {'result': 'invalid role'}, 406
		else:
			Accounts.accounts.append(self.items)
			return 1
