from .verify import Verification
from .products import Products, products
from .users import Accounts


sales = []

class Sales(Verification):
	def __init__(self,items):
		self.items = items

	def check_sales_input(self):
		items = self.items
		if self.is_sales_payload(items) is False:
			return {'result': 'invalid payload'},406
		elif items['quantity'] < 1:
			return {'result': 'quantity can not be less than one'},406
		elif items['productId'] < 0:
			return {'result': 'productId can not be less than zero'},406
		else:
			return 1
	
	def add_sales(self):
		items = self.items
		pid = Products.get_one(items['productId'])
		total = pid[items['productId']]['price'] * items['quantity']
		items['total'] = total
		for product in products:
			rem = product['quantity'] - self.items['quantity']
			bal = self.items['quantity'] - product['quantity']
			if product['quantity'] == 0:
				return {'message': 'Out of stock'},404
			elif  rem < 0:
				return [{'message': 'only {} items in inventory'.format(product['quantity'])},
				{'error':'{} more than required'.format(bal)}],406
			else:
				items['unit price'] = product['price']
				sales.append(items)
				items['userId'] = Accounts.get_id()[0]['id']
				product['quantity'] -= self.items['quantity']
				return {'result': 'item has been sold'},201
