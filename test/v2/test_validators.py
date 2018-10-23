import unittest

from app.api.v2.model.verify import Verify


class TestValidators(unittest.TestCase):
	def setUp(self):
		self.obj = Verify()

	def tearDown(self):
		self.obj = None

	def test_empty_data(self):
		test = self.obj.is_empty(['','d'])
		self.assertEqual(test,1)

	def test_is_whitespace(self):
		test = self.obj.is_whitespace(['  ','d'])
		self.assertEqual(test,1)

	def test_is_not_payload(self):
		test = self.obj.is_payload({'name':'dad','age':9},['name','age','class'])
		self.assertEqual(test,1)

	def test_is_not_email(self):
		test = self.obj.is_email('notmail.com')
		self.assertEqual(test,1)

	def test_less_than(self):
		test = self.obj.less_than(2,1)
		self.assertEqual(test,1)