# Writing unit-test for the searching algorithms
import unittest

'''Test cases for searching functions'''
from searching import binary_search, ternary_search

import unittest

class MyTest(unittest.TestCase):
	def setUp(self):
		self.array = [2, 5, 6, 12, 17, 23, 34, 45, 67, 81]
		self.high = len(self.array)
		self.key = 23

	def test_binary_search(self):
		self.assertEqual(binary_search.binary_search(0, self.high, self.key, self.array), 5)

	def test_ternary_search(self):
		self.assertEqual(ternary_search.ternary_search(0, self.high, self.key, self.array), 5)
