from .verify import Verification


products = []

class Products(Verification):
	def __init__(self,items):
		self.items = items

	def check_product_input(self):
		payload=self.is_product_payload(self.items) 
		strings = [self.items['name'],self.items['category']]
		if payload is False:
			return {'result':'invalid payload'},406
		elif self.is_empty(strings) is True:
			return {'result': 'data set is empty'},406
		elif self.is_whitespace(strings) is True:
			return {'result': 'data set contains only white space'},406
		elif self.items['quantity'] < 1:
			return {'result': 'quantity can not be less than one'},406
		elif self.items['price'] < 1:
			return {'result': 'price can not be less than one'},406
		else:
			return 1

	def add_product(self):
		self.items['id'] = len(products)
		for product in products:
			if product['name'] == self.items['name']:
				product['quantity'] += self.items['quantity']
				return {'result': 'product quantity has been increased'},201
		products.append(self.items)
		return {'result': 'product has added to database'},201

	@classmethod
	def get_all(cls):
		if len(products) == 0:
			return {'result': 'no products found'},404
		else:
			return [{'message': 'all products'},products],200

	@classmethod
	def get_one(cls,productId):
		if len(products) == 0:
			return {'result': 'no products found'},404
		else:
			return products[productId],200