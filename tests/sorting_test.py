# coding: UTF-8

'''Test cases for sorting functions'''

import unittest

from sorting import bubble_sort, selection_sort, insertion_sort, merge_sort

class MyTest(unittest.TestCase):
	def setUp(self):
		self.array = [34, 45, 2, 6, 64, 3, 17, 12, 23,  67, 81, 8]
		self.sorted_array = [2, 3, 6, 8, 12, 17, 23, 34, 45, 64, 67, 81]

	def test_bubble_sort(self):
		self.assertEqual(bubble_sort.bubble_sort(self.array), self.sorted_array)

	def test_insertion_sort(self):
		self.assertEqual(insertion_sort.insertion_sort(self.array), self.sorted_array)

	def test_merge_sort(self):
		self.assertEqual(merge_sort.merge_sort(self.array), self.sorted_array)

	def test_selection_sort(self):
		self.assertEqual(selection_sort.selection_sort(self.array), self.sorted_array)
