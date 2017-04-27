# coding: UTF-8

'''
	Insertion sort

	Insertion sort is based on the idea that one element from the input elements is consumed in each iteration to find 
	its correct position i.e. the position to which it belongs in a sorted array.

	Time complexity: O(n*n)
'''

def insertion_sort(array):

	for i in range(1, len(array)):

		current_value = array[i]
		position = i

		while ( position > 0 and current_value < array[position-1]):
			array[position] = array[position-1]
			position = position-1

		array[position] = current_value

	return array

# Writing unit-test for the above function
import unittest

class MyTest(unittest.TestCase):
	def setUp(self):
		self.array = [34, 45, 2, 6, 64, 3, 17, 12, 23,  67, 81, 8]

	def test(self):
		self.assertEqual(insertion_sort(self.array), [2, 3, 6, 8, 12, 17, 23, 34, 45, 64, 67, 81])

if __name__ == "__main__":
	unittest.main()