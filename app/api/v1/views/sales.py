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
		return {'testing':'testing'}

	@ns_sales.expect(mod)
	def post(self):
		try:
			data =request.get_json()
			pid = Products.get_one(data['productId'])
			total = pid[data['productId']]['price'] * data['quantity']
			data['price'] = total
			obj = Sales(data)
			if obj.check_user_input() == 1:
				Sales.sales.append(data)
				return {'result': 'sales added'}
			else:
				return obj.check_user_input()
		except KeyError:
			return {'result':'invalid product id'},404


@ns_sales.route('/<saleId>')
class getOne(Resource):
	"""
	class contains http method get
	for getting	one sale record
	"""
	def get(self,saleId):
		return {'testing':'testing'}