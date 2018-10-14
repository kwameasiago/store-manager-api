from flask import request
from flask_restplus import Namespace, Resource, fields

ns_product = Namespace('products',description='Routes related to products')


@ns_product.route('/')
class AllProduct(Resource):
	def get(self):
		return {'testing':'testing'},200

	def post(self):
		return {'testing':'testing'},200


@ns_product.route('/<productId>')
class OneProduct(Resource):
	def get(self,id):
		return {'testing':'testing'},200