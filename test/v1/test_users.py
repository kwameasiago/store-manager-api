import unittest
import json

from app import create_app


class TestInvalidData(unittest.TestCase):
	def setUp(self):
		self.test = create_app('testing').test_client()
		self.content_type = 'application/json'

	def tearDown(self):
		self.test = None
		self.content_type = None


	def test_not_emailI(self):
		payload = {'password': '1234', 'email': 'stringgmail.com'}
		response = self.test.post('/api/v1/users/login',content_type=self.content_type,
			data=json.dumps(payload))
		data =json.loads(response.get_data().decode('UTF-8'))
		self.assertEqual(response.status_code,406)
		self.assertEqual(data,{'result': 'invalid email'})

	def test_invalid_login(self):
		payload = {'password': 'notpassword', 'email': 'not@gmail.com'}
		response = self.test.post('/api/v1/users/login',content_type=self.content_type,
			data=json.dumps(payload))
		data =json.loads(response.get_data().decode('UTF-8'))
		self.assertEqual(response.status_code,406)
		self.assertEqual(data,{'result': 'email or password invalid'})

class TestValidData(unittest.TestCase):
	def setUp(self):
		self.test = create_app('testing').test_client()
		self.content_type = 'application/json'
		payload = {'password': '1234', 'email': 'admin@gmail.com'}
		response = self.test.post('/api/v1/users/login',content_type=self.content_type,
			data=json.dumps(payload))
		data =json.loads(response.get_data().decode('UTF-8'))
		token = data[1]['token']
		self.headers = {'X-API-KEY':'{}'.format(token)}

	def tearDown(self):
		self.test = None
		self.content_type = None

	def test_login(self):
		payload = {'password': '1234', 'email': 'admin@gmail.com'}
		response = self.test.post('/api/v1/users/login',content_type=self.content_type,
			data=json.dumps(payload))
		data =json.loads(response.get_data().decode('UTF-8'))
		self.assertEqual(response.status_code,200)

	def test_register_employee(self):
		payload = {'role': 'admin', 'last_name': 'string', 'password': '1234', 'email': 'string@gmail.com',
		 'first_name': 'string'}
		response = self.test.post('/api/v1/users/register',content_type=self.content_type,
			data=json.dumps(payload),headers=self.headers)
		data =json.loads(response.get_data().decode('UTF-8'))
		self.assertEqual(response.status_code,200)

if __name__ == '__main__':
	unittest.main()