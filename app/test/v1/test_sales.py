import unittest
import json

from ... import create_app

class TestInvalidData(unittest.TestCase):
	"""
	class to test sales endpoint invalid data
	"""
	def setUp(self):
		self.test = create_app().test_client()
		self.content_type = 'application/json'

	def tearDown(self):
		self.test = None
		self.content_type = None


	# test if input is empty
	def test_empty_sales(self):
		payload = {'name':'','quantity':10}
		response = self.test.post('/sales/',content_type=self.content_type,
			data=json.dumps(payload))
		data = json.loads(response.get_data().decode('UTF-8'))
		self.assertEqual(response.status_code,406)
		self.assertEqual(data,{'result': 'Empty Input'})

	# test when input contains only white space
	def test_white_space_sales(self):
		payload = {'name':'  ','quantity':10}
		response = self.test.post('/sales/',content_type=self.content_type,
			data=json.dumps(payload))
		data = json.loads(response.get_data().decode('UTF-8'))
		self.assertEqual(response.status_code,406)
		self.assertEqual(data,{'result': 'Input contains only whitespace'})

	# test if user enter an invalid json  payload
	def test_invalid_payload(self):
		payload = {'name':'omo','quantity':10,'xyz':''}
		response = self.test.post('/sales/',content_type=self.content_type,
			data=json.dumps(payload))
		data = json.loads(response.get_data().decode('UTF-8'))
		self.assertEqual(response.status_code,406)
		self.assertEqual(data,{'result':'Invalid json object'})

	# test if user enters an invalid data type
	def test_invalid_data_type(self):
		payload = {'name':'omo','quantity':'0'}
		response = self.test.post('/sales/',content_type=self.content_type,
			data=json.dumps(payload))
		data = json.loads(response.get_data().decode('UTF-8'))
		self.assertEqual(response.status_code,406)
		self.assertEqual(data,{'result': 'Invalid json object'})

	# test quantity less than 1
	def test_min_quantity(self):
		payload = {'name':'omo','quantity':-90}
		response = self.test.post('/sales/',content_type=self.content_type,
			data=json.dumps(payload))
		data = json.loads(response.get_data().decode('UTF-8'))
		self.assertEqual(response.status_code,406)
		self.assertEqual(data,{'result':'Invalid Quantity'})

	# test if id is invalids
	def test_invalid_sales_id(self):
		response =self.test.get('/sales/{}'.format(12),content_type=self.content_type)
		data = json.loads(response.get_data().decode('UTF-8'))
		self.assertEqual(response.status_code,404)
		self.assertEqual(data,{'result':'Invalid sales id'})


class TestValidData(unittest.TestCase):
	"""
	class to test sales endpoints valid data
	"""
	def setUp(self):
		self.test = create_app().test_client()
		self.content_type = 'application/json'
		self.payload = {'name':'omo','quantity':10}


	def tearDown(self):
		self.test = None
		self.content_type = None

	# test posting new sales
	def test_post_sales_data(self):
		response = self.test.post('/sales/',content_type=self.content_type,
			data=json.dumps(self.payload))
		data = json.loads(response.get_data().decode('UTF-8'))
		self.assertEqual(response.status_code,201)
		self.assertEqual(data,{'result':'sales added'})


	# test geting all sales
	def test_get_all_sales(self):
		response = self.test.get('/sales/',content_type=self.content_type)
		self.assertEqual(response.status_code,200)

	# test if no sales found
	def test_no_sales_found(self):
		response = self.test.get('/sales/',content_type=self.content_type)
		data = json.loads(response.get_data().decode('UTF-8'))
		self.assertEqual(response.status_code,404)
		self.assertEqual(data,{'result':'no sales found'})

	# test getting one sales
	def test_get_one_sales(self):
		self.test.post('/sales/',content_type=self.content_type,
			data=json.dumps(self.payload))
		response = self.test.get('/sales/0',content_type=self.content_type)
		self.assertEqual(response.status_code,200)






if __name__ == '__main__':
	unittest.main()