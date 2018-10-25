import unittest

from app.api.v1.model.verify import Verification

class TestVerification(unittest.TestCase):
	"""
	class to test verification
	"""
	def setUp(self):
		self.obj = Verification()

	def tearDown(self):
		self.obj = None

	# test empty data
	def test_is_empty(self):
		test = self.obj.is_empty(['','dad'])
		self.assertEqual(test,0)

	# if data is not emoty
	def test_not_empty(self):
		test = self.obj.is_empty(['fs','fs'])
		self.assertFalse(test)

	# test if white space
	def test_is_whitespace(self):
		test = self.obj.is_whitespace(['  ','d'])
		self.assertEqual(test,0)

	# test if not whitespace
	def test_not_whitespace(self):
		test = self.obj.is_whitespace(['d','df'])
		self.assertFalse(test)

	# test correct product payload
	def test_is_product_payload(self):
		payload = {'name':'omo','moq':3,'quantity':0,'category':0,'price':0}
		test = self.obj.is_product_payload(payload)
		self.assertTrue(test)

	# test incorrect payload
	def test_not_payload(self):
		payload = {'name':'omo','moq':3,'quantity':0,'qwr':0}
		payload_2 = {'name':'omo','moq':3}
		payload_3 = {'name':'omo','moq':3,'quantity':0,'category':0,'we':0}
		test = self.obj.is_product_payload(payload)
		test_2 = self.obj.is_product_payload(payload_2)
		test_3 = self.obj.is_product_payload(payload_3)
		self.assertFalse(test)
		self.assertFalse(test_2)
		self.assertFalse(test_3)

if __name__ == '__main__':
	unittest.main()