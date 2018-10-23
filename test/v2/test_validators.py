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
		self.assertEqual(test,1)

	# test if whitespace exists
	def test_is_whitespace(self):
		test = self.obj.is_whitespace(['  ','d'])
		self.assertEqual(test,1)

	# test if item is not a playload
	def test_is_not_payload(self):
		test = self.obj.is_payload({'name':'dad','age':9},['name','age','class'])
		self.assertEqual(test,1)

	# test if item is not an email
	def test_is_not_email(self):
		test = self.obj.is_email('notmail.com')
		self.assertEqual(test,1)

	# test if num1 is less than num 2
	def test_less_than(self):
		test = self.obj.less_than(2,1)
		self.assertEqual(test,1)
