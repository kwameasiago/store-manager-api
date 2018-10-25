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
		pid = products[self.items['productId']]
		total = pid['price'] * self.items['quantity']
		self.items['total'] = total
		rem = pid['quantity'] - self.items['quantity']
		bal = self.items['quantity'] - pid['quantity']
		if pid['quantity'] == 0:
			return {'message': 'Out of stock'},404
		elif  rem < 0:
			return [{'message': 'only {} items in inventory'.format(pid['quantity'])},
			{'error':'{} more than required'.format(bal)}],406
		else:
			self.items['unit price'] = pid['price']
			sales.append(self.items)
			self.items['userId'] = Accounts.get_id()[0]['id']
			pid['quantity'] -= self.items['quantity']
			return {'result': 'item has been sold'},201
