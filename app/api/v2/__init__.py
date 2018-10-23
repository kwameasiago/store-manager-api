from flask import Blueprint
from flask_restplus import Api

from .views.products import ns_product
from .views.sales import ns_sales
from .views.users import ns_users

authorizations = {
    'apikey': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'X-API-KEY'
    }
}

app_v1 = Blueprint('app_v1',__name__,url_prefix='/api/v1')
api_v1 = Api(app_v1,title='Store Manager',version='1.0',description='Store management api v1',
	authorizations=authorizations)


api_v1.add_namespace(ns_product)
api_v1.add_namespace(ns_sales)
api_v1.add_namespace(ns_users)