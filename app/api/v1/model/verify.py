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

	def payload(self,items,length,keys):
		items = items.keys()
		if len(items) == length:
			for item in items:
				if item not in keys:
					return False
			return True
		else:
			return False

	def is_product_payload(self,items):
		res = self.payload(items,5,['name','category','moq','quantity','price'])
		return res

	def is_sales_payload(self,items):
		res = self.payload(items,3,['productId','quantity','price'])
		return res

	def is_login_payload(self,items):
		res = self.payload(items,3,['email','role','password'])
		return res

	def is_register_payload(self,items):
		res = self.payload(items,5,['first_name','last_name','email','role','password'])
		return  res

	def is_email(self,email):
		result = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', email)
		if result is None:
			res = True
		else:
			res = False
		return res


