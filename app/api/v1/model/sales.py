from .verify import Verification
from .products import Products


class Sales(Verification):
	sales = []
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
		items['price'] = total
		Sales.sales.append(items)
		return {'result': 'sales added'},201
