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

