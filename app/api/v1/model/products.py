from .verify import Verification


class Products(Verification):
	products = []
	def __init__(self,items):
		self.items = items

	def check_user_input(self):
		payload=self.is_product_payload(self.items) 
		if payload is False:
			return {'result':'invalid payload'},406
		elif self.is_empty([self.items['name'],self.items['category']]) is True:
			return {'result': 'data set is empty'},406
		elif self.is_whitespace([self.items['name'],self.items['category']]) is True:
			return {'result': 'data set contains only white space'},406
		elif self.items['quantity'] < 1:
				return {'result': 'quantity can not be less than one'},406
		else:
			return 1

	def add_product(self):
		self.items['id'] = len(Products.products)
		Products.products.append(self.items)
		return {'result': 'product added'},201

	@classmethod
	def get_all(cls):
		if len(Products.products) == 0:
			return {'result': 'no products found'},404
		else:
			return Products.products,200