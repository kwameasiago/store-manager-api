import unittest
import json

from ... import create_app
from ...api.v1.model.products import Products

class TestInvalidData(unittest.TestCase):
	"""
	class to test products endpoint
	"""
	def setUp(self):
		self.test = create_app('testing').test_client()
		self.content_type = 'application/json'
		payload = {'role': 'admin', 'password': '1234', 'email': 'admin@gmail.com'}
		response = self.test.post('/users/login',content_type=self.content_type,
			data=json.dumps(payload))
		data =json.loads(response.get_data().decode('UTF-8'))
		token = data['result']
		self.headers = {'X-API-KEY':'{}'.format(token)}

	def tearDown(self):
		self.test = None
		self.content_type = None


	# test if input is empty
	def test_empty_products(self):
		payload = {'name': '', 'quantity': 1, 'category': 'furniture','moq':1,'price':100}
		response = self.test.post('/products/',content_type=self.content_type,
			data=json.dumps(payload),headers=self.headers)
		data = json.loads(response.get_data().decode('UTF-8'))
		self.assertEqual(response.status_code,406)
		self.assertEqual(data,{'result': 'data set is empty'})

	# test when input contains only white space
	def test_white_space_products(self):
		payload = {'name': '  ', 'quantity': 1, 'category': 'furniture','moq':1,'price':100}
		response = self.test.post('/products/',content_type=self.content_type,
			data=json.dumps(payload),headers=self.headers)
		data = json.loads(response.get_data().decode('UTF-8'))
		self.assertEqual(response.status_code,406)
		self.assertEqual(data,{'result': 'data set contains only white space'})

	# test if user enter an invalid json  payload
	def test_invalid_payload(self):
		payload = {'name': 'omo', 'quantity': 1, 'category': 'furniture','moq':1,'xyz':'','price':100}
		response = self.test.post('/products/',content_type=self.content_type,
			data=json.dumps(payload),headers=self.headers)
		data = json.loads(response.get_data().decode('UTF-8'))
		self.assertEqual(response.status_code,406)
		self.assertEqual(data,{'result':'invalid payload'})

	# test if user enters an invalid data type
	def test_invalid_data_type(self):
		payload = {'name': 'omo', 'quantity': 1, 'category': 'furniture','moq':'0','price':100}
		response = self.test.post('/products/',content_type=self.content_type,
			data=json.dumps(payload),headers=self.headers)
		data = json.loads(response.get_data().decode('UTF-8'))
		self.assertEqual(response.status_code,400)
		self.assertEqual(data['message'],'Input payload validation failed')

	# test quantity less than 1
	def test_min_quantity(self):
		payload = {'name': 'omo', 'quantity': -21, 'category': 'furniture','moq':0,'price':100}
		response = self.test.post('/products/',content_type=self.content_type,
			data=json.dumps(payload),headers=self.headers)
		data = json.loads(response.get_data().decode('UTF-8'))
		self.assertEqual(response.status_code,406)
		self.assertEqual(data,{'result':'quantity can not be less than one'})

	def test_invalid_products_id(self):
		response =self.test.get('/products/-12',content_type=self.content_type,headers=self.headers)
		data = json.loads(response.get_data().decode('UTF-8'))
		self.assertEqual(response.status_code,404)
		self.assertEqual(data,{'result':'no products found'})

	def test_min_price(self):
		payload = {'name': 'omo', 'quantity': 21, 'category': 'furniture','moq':0,'price':0}
		response = self.test.post('/products/',content_type=self.content_type,
			data=json.dumps(payload),headers=self.headers)
		data = json.loads(response.get_data().decode('UTF-8'))
		self.assertEqual(response.status_code,406)
		self.assertEqual(data,{'result':'price can not be less than one'})


class TestValidData(unittest.TestCase):
	def setUp(self):
		self.test = create_app('testing').test_client()
		self.content_type = 'application/json'
		self.payload = {'name': 'omo', 'quantity': 1, 'category': 'furniture','moq':0,'price':100}
		payload = {'role': 'admin', 'password': '1234', 'email': 'admin@gmail.com'}
		response = self.test.post('/users/login',content_type=self.content_type,
			data=json.dumps(payload))
		data =json.loads(response.get_data().decode('UTF-8'))
		token = data['result']
		self.headers = {'X-API-KEY':'{}'.format(token)}


	def tearDown(self):
		self.test = None
		self.content_type = None
		Products.products.clear()

	def test_post_products_data(self):
		response = self.test.post('/products/',content_type=self.content_type,
			data=json.dumps(self.payload),headers=self.headers)
		data = json.loads(response.get_data().decode('UTF-8'))
		self.assertEqual(response.status_code,201)
		self.assertEqual(data,{'result':'product added'})


	def test_get_all_products(self):
		post = self.test.post('/products/',content_type=self.content_type,
			data=json.dumps(self.payload),headers=self.headers)
		self.assertEqual(post.status_code,201)
		response = self.test.get('/products/',content_type=self.content_type,headers=self.headers)
		self.assertEqual(response.status_code,200)

	def test_no_products_found(self):
		response = self.test.get('/products/',content_type=self.content_type,headers=self.headers)
		data = json.loads(response.get_data().decode('UTF-8'))
		self.assertEqual(response.status_code,404)
		self.assertEqual(data,{'result':'no products found'})

	def test_get_one_products(self):
		post = self.test.post('/products/',content_type=self.content_type,
			data=json.dumps(self.payload),headers=self.headers)
		self.assertEqual(post.status_code,201)
		response = self.test.get('/products/{}'.format(0),content_type=self.content_type,
			headers=self.headers)
		self.assertEqual(response.status_code,200)






if __name__ == '__main__':
	unittest.main()