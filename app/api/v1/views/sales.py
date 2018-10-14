from flask import request
from flask_restplus import Namespace, Resource, fields


ns_sales = Namespace('sales',description='Sales Endpoints')


@ns_sales.route('/')
class GetAll(Resource):
	"""
	Class contains get and post http method
	for sales record
	"""
	def get(self):
		return {'testing':'testing'}

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