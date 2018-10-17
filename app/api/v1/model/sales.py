from .verify import Verification


class Sales(Verification):
	sales = []
	def __init__(self,items):
		self.items = items

	def check_user_input(self):
		if self.is_sales_payload(self.items) is False:
			return {'result': 'invalid payload'},406
		elif self.items['quantity'] < 1:
			return {'result': 'quantity can not be less than one'},406
		elif self.items['productId'] < 0:
			return {'result': 'productId can not be less than zero'},406
		else:
			return 1
