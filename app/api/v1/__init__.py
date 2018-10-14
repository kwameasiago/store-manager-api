from flask import Blueprint
from flask_restplus import Api

from .views.products import ns_product
from .views.sales import ns_sales

app_v1 = Blueprint('app_v1',__name__)
api_v1 = Api(app_v1)


api_v1.add_namespace(ns_product)
api_v1.add_namespace(ns_sales)