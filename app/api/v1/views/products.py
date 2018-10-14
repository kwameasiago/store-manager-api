from flask import request
from flask_restplus import Namespace, Resource, fields

ns_product = Namespace('products',description='Products endpoints')

mod = ns_product.model('product model',{
	'name': fields.String(description='products Name'),
	'quantity': fields.Integer(description='Products quantity'),
	'moq':fields.Integer(description='Minimum Inventory Quantity'),
	'catefory': fields.String(description='category of product')
	})


@ns_product.route('/')
class AllProduct(Resource):
	"""
	class contains http method get and post 
	for getting  sales record
	"""
	def get(self):
		return {'testing':'testing'},200

	@ns_product.expect(mod)
	def post(self):
		return {'testing':'testing'},200


@ns_product.route('/<productId>')
class OneProduct(Resource):
	"""
	class contains http method get
	for getting one products
	"""
	def get(self,id):
		return {'testing':'testing'},200