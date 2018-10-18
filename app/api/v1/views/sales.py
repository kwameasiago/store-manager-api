from flask import request
from flask_restplus import Namespace, Resource, fields

from ..model.sales import Sales
from ..model.products import Products


ns_sales = Namespace('sales',description='Sales Endpoints')

mod = ns_sales.model('sales model',{
	'productId': fields.Integer(description='Name of product sold'),
	'quantity': fields.Integer(description='Quantity of product sold')
	})


@ns_sales.route('/')
class GetAll(Resource):
	"""
	Class contains get and post http method
	for sales record
	"""
	def get(self):
		sales = len(Sales.sales)
		if sales < 1:
			return {'result':'no sales found'},404
		else:
			return Sales.sales,200

	@ns_sales.expect(mod,validate=True)
	def post(self):
		data =request.get_json()
		obj = Sales(data)
		data['price'] = 0
		if obj.check_sales_input() == 1:
			try:
				return obj.add_sales()
			except IndexError:
				return {'result':'invalid product id'},406
			except KeyError:
				return {'result': 'invalid product id'},406
		else:
				return obj.check_sales_input()

@ns_sales.route('/<saleId>')
class getOne(Resource):
	"""
	class contains http method get
	for getting	one sale record
	"""
	def get(self,saleId):
		try:
			return Sales.sales[int(saleId)]
		except IndexError:
			return {'result': 'sales does not exist'},404
