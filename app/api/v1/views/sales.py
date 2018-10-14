from flask import request
from flask_restplus import Namespace, Resource, fields


ns_sales = Namespace('sales',description='Sales Endpoints')


@ns_sales.route('/')
class GetAll(Resource):
	def get(self):
		return {'testing':'testing'}

	def post(self):
		return {'testing': 'testing'}


@ns_sales.route('/<saleId>')
class getOne(Resource):
	def get(self,saleId):
		return {'testing':'testing'}