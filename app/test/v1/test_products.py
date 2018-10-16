import unittest
import json

from ... import create_app

class TestInvalidData(unittest.TestCase):
	"""
	class to test sales endpoint
	"""
	def setUp(self):
		self.test = create_app('testing').test_client()
		self.content_type = 'application/json'

	def tearDown(self):
		self.test = None
		self.content_type = None


	# test if input is empty
	def test_empty_sales(self):
		payload = {'name': '', 'quantity': 1, 'category': 'furniture','moq':1,'price':100}
		response = self.test.post('/products/',content_type=self.content_type,
			data=json.dumps(payload))
		data = json.loads(response.get_data().decode('UTF-8'))
		self.assertEqual(response.status_code,406)
		self.assertEqual(data,{'result': 'data set is empty'})

	# test when input contains only white space
	def test_white_space_sales(self):
		payload = {'name': '  ', 'quantity': 1, 'category': 'furniture','moq':1,'price':100}
		response = self.test.post('/products/',content_type=self.content_type,
			data=json.dumps(payload))
		data = json.loads(response.get_data().decode('UTF-8'))
		self.assertEqual(response.status_code,406)
		self.assertEqual(data,{'result': 'data set contains only white space'})

	# test if user enter an invalid json  payload
	def test_invalid_payload(self):
		payload = {'name': 'omo', 'quantity': 1, 'category': 'furniture','moq':1,'xyz':'','price':100}
		response = self.test.post('/products/',content_type=self.content_type,
			data=json.dumps(payload))
		data = json.loads(response.get_data().decode('UTF-8'))
		self.assertEqual(response.status_code,406)
		self.assertEqual(data,{'result':'invalid payload'})

	# test if user enters an invalid data type
	def test_invalid_data_type(self):
		payload = {'name': 'omo', 'quantity': 1, 'category': 'furniture','moq':'0','price':100}
		response = self.test.post('/products/',content_type=self.content_type,
			data=json.dumps(payload))
		data = json.loads(response.get_data().decode('UTF-8'))
		self.assertEqual(response.status_code,400)
		self.assertEqual(data['message'],'Input payload validation failed')

	# test quantity less than 1
	def test_min_quantity(self):
		payload = {'name': 'omo', 'quantity': -21, 'category': 'furniture','moq':0,'price':100}
		response = self.test.post('/products/',content_type=self.content_type,
			data=json.dumps(payload))
		data = json.loads(response.get_data().decode('UTF-8'))
		self.assertEqual(response.status_code,406)
		self.assertEqual(data,{'result':'quantity can not be less than one'})

	def test_invalid_sales_id(self):
		response =self.test.get('/products/-12',content_type=self.content_type)
		data = json.loads(response.get_data().decode('UTF-8'))
		self.assertEqual(response.status_code,404)
		self.assertEqual(data,{'result':'Invalid sales id'})


class TestValidData(unittest.TestCase):
	def setUp(self):
		self.test = create_app('testing').test_client()
		self.content_type = 'application/json'
		self.payload = {'name': 'omo', 'quantity': 1, 'category': 'furniture','moq':0,'price':100}


	def tearDown(self):
		self.test = None
		self.content_type = None

	def test_post_sales_data(self):
		response = self.test.post('/products/',content_type=self.content_type,
			data=json.dumps(self.payload))
		data = json.loads(response.get_data().decode('UTF-8'))
		#self.assertEqual(response.status_code,201)
		self.assertEqual(data,{'result':'product added'})


	def test_get_all_sales(self):
		response = self.test.get('/products/',content_type=self.content_type)
		self.assertEqual(response.status_code,200)

	def test_no_sales_found(self):
		response = self.test.get('/products/',content_type=self.content_type)
		data = json.loads(response.get_data().decode('UTF-8'))
		self.assertEqual(response.status_code,404)
		self.assertEqual(data,{'result':'no products found'})

	def test_get_one_sales(self):
		response = self.test.get('/product/',content_type=self.content_type)
		self.assertEqual(response.status_code,200)






if __name__ == '__main__':
	unittest.main()