from flask import request
from flask_restplus import Namespace, Resource, fields


ns_sales = Namespace('sales',description='Sales Endpoints')

mod = ns_sales.model('sales model',{
	'name': fields.String(description='Name of product sold'),
	'quantity': fields.String(description='Quantity of product sold')
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
		return {'testing': 'testing'}


@ns_sales.route('/<saleId>')
class getOne(Resource):
	"""
	class contains http method get
	for getting	one sale record
	"""
	def get(self,saleId):
		return {'testing':'testing'}