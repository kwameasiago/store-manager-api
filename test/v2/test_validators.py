import unittest

from app.api.v2.model.verify import Verify


class TestValidators(unittest.TestCase):
	"""
	class to test user inputs
	"""
	def setUp(self):
		self.obj = Verify()

	def tearDown(self):
		self.obj = None

	# test if data is empty
	def test_empty_data(self):
		test = self.obj.is_empty(['','d'])
		self.assertEqual(test,{'error': 'empty data set detected'})

	# test if data is not empty
	def test_not_empty_data(self):
		test = self.obj.is_empty(['d','d'])
		self.assertEqual(test,1)

	# test if whitespace does not  exists
	def test_is_whitespace(self):
		test = self.obj.is_whitespace(['  ','d'])
		self.assertEqual(test,{'error': 'whitespace data detected'})

	# test if whitespace exists
	def test_is_not_whitespace(self):
		test = self.obj.is_whitespace(['s','d'])
		self.assertEqual(test,1)

	# test if item is not a playload
	def test_is_not_payload(self):
		test = self.obj.is_payload({'name':'dad','age':9},['name','age','class'])
		self.assertEqual(test,{'error': 'invalid payload'})

	# test if item is a playload
	def test_is_not_payload(self):
		test = self.obj.is_payload({'name':'dad','age':9, 'class':3},['name','age','class'])
		self.assertEqual(test,1)

	# test if item is not an email
	def test_is_not_email(self):
		test = self.obj.is_email('notmail.com')
		self.assertEqual(test, {'error': 'invalid email detected'})

	# test if item is an email
	def test_is_email(self):
		test = self.obj.is_email('mail@gmail.com')
		self.assertEqual(test, 1)

	# test if num1 is less than num 2
	def test_less_than(self):
		test = self.obj.less_than(2,11)
		self.assertTrue(test)
