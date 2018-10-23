import re

class Verify:
	"""
	class to verify inputs
	"""
	def is_empty(self,items):
		for item in items:
			if bool(item) is False:
				return {'error': 'empty data set detected'}
		return  1

	def is_whitespace(self,items):
		for item in items:
			if item.isspace() is True:
				return {'error': 'whitespace data detected'}
		return 1


	def is_payload(self,items,keys):
		items = items.keys()
		if len(items) == len(keys):
			for item in items:
				if item not in keys:
					return {'error': 'invalid payload'}
			return 1
		else:
			return {'error': 'invalid payload'}

	def is_email(self,email):
		result = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', email)
		if result is None:
			res = {'error': 'invalid email detected'}
		else:
			res = 1
		return res

	def less_than(self,num1,num2):
		if num1 < num2:
			res = True
		else:
			res = False
		return res

