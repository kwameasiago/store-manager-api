from flask import request
from flask_restplus import Namespace, Resource, fields

from ..model.products import Products
from ..utils.auth import token_required


ns_product = Namespace('products',description='Products endpoints')

mod = ns_product.model('product model',{
	'name': fields.String(description='products Name'),
	'quantity': fields.Integer(description='Products quantity'),
	'moq':fields.Integer(description='Minimum Inventory Quantity'),
	'category': fields.String(description='Category of product'),
	'price': fields.Integer(description='Price of product')
	})


@ns_product.route('/')
class AllProduct(Resource):
	"""
	class contains http method get and post 
	for getting  sales record
	"""
	@token_required
	@ns_product.doc(security='apikey')
	def get(self):
		return Products.get_all()

	@ns_product.expect(mod,validate=True)
	@token_required
	@ns_product.doc(security='apikey')
	def post(self):
		data = request.get_json()
		obj = Products(data)
		if obj.check_product_input() == 1:
			return obj.add_product()
		else:
			return obj.check_product_input()


@ns_product.route('/<productId>')
class OneProduct(Resource):
	"""
	class contains http method get
	for getting one products
	"""
	@token_required
	@ns_product.doc(security='apikey')
	def get(self,productId):
		try:
			return Products.get_one(int(productId))
		except IndexError:
			return {'result':'no products found'},404
