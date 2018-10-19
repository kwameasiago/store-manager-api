import re


class Verification:
	"""
	class to verify data
	"""
	def is_empty(self,items):
		for item in items:
			if bool(item) is False:
				return True
		return False

	def is_whitespace(self,items):
		for item in items:
			if item.isspace() is True:
				return True
		return False

	def is_product_payload(self,items):
		items = items.keys()
		if len(items) == 5:
			product_keys = ['name','category','moq','quantity','price']
			for item in items:
				if item not in product_keys:
					return False
			return True
		else:
			return False

	def is_sales_payload(self,items):
		items, sales_keys = items.keys(), ['productId','quantity','price']
		res = None
		if len(items) == 3:
			for item in items:
				if item not in sales_keys:
					res = False
			res = True
		else:
			res = False
		return res

	def is_login_payload(self,logs):
		logs, login_keys = logs.keys(),['email','role','password']
		if len(logs) == 3:
			for log in logs:
				if log not in login_keys:
					res = False
			res = True
		else:
			res = False
		return res

	def is_register_payload(self,items):
		items, register_keys = items.keys(),['first_name','last_name','email','role','password']
		if len(items) == 5:
			for item in items:
				if item not in register_keys:
					res = False
			res = True
		else:
			res = False
		return res


	def is_email(self,email):
		result = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', email)
		if result is None:
			res = True
		else:
			res = False
		return res


