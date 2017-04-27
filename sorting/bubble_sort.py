# coding: UTF-8

'''
	Bubble Sort

	Bubble sort is based on the idea of repeatedly comparing pairs of adjacent elements and then swapping their positions if 
	they exist in the wrong order.

	Complexity: O(n*n)
'''

def bubble_sort(array):

	for i in range(len(array)-1):
		for j in range(i, len(array)):
			if array[i] > array[j]:
				array[i], array[j] = array[j], array[i]

	return array

# Writing unit-test for the above function
import unittest

class MyTest(unittest.TestCase):
	def setUp(self):
		self.array = [34, 45, 2, 6, 64, 3, 17, 12, 23,  67, 81, 8]

	def test(self):
		self.assertEqual(bubble_sort(self.array), [2, 3, 6, 8, 12, 17, 23, 34, 45, 64, 67, 81])

if __name__ == "__main__":
	unittest.main()