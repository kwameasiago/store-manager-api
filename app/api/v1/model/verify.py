import re


class Verification:
	"""
	class to verify data
	"""
	def is_empty(self,items):
		for item in items:
			if bool(item) is False:
				return items.index(item)
		return False

	def is_whitespace(self,items):
		for item in items:
			if item.isspace() is True:
				return items.index(item)
		return False

	def payload(self,items,keys):
		items = items.keys()
		if len(items) == len(keys):
			for item in items:
				if item not in keys:
					return False
			return True
		else:
			return False

	def is_product_payload(self,items):
		res = self.payload(items,['name','category','moq','quantity','price'])
		return res

	def is_sales_payload(self,items):
		res = self.payload(items,['productId','quantity','total'])
		return res

	def is_login_payload(self,items):
		res = self.payload(items,['email','password'])
		return res

	def is_register_payload(self,items):
		res = self.payload(items,['first_name','last_name','email','role','password'])
		return  res

	def is_email(self,email):
		result = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', email)
		if result is None:
			res = True
		else:
			res = False
		return res


