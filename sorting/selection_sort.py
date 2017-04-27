# coding: UTF-8

'''
	Selection sort

	The Selection sort algorithm is based on the idea of finding the minimum or maximum element in an unsorted array 
	and then putting it in its correct position in a sorted array.

	Complexity: O(n*n)
'''

def selection_sort(array):
	''' Sort a list using selection sort algorithm'''
	for i, _ in enumerate(array):
		# Initialize smallest element and index
		index = i
		for j in range(i, len(array)):
			if array[j] < array[index]:
				index = j
		
		if index != i:
			array[i], array[index] = array[index], array[i]

	return array


# Writing unit-test for the above function
import unittest

class MyTest(unittest.TestCase):
	def setUp(self):
		self.array = [34, 45, 2, 6, 64, 3, 17, 12, 23,  67, 81, 8]

	def test(self):
		self.assertEqual(selection_sort(self.array), [2, 3, 6, 8, 12, 17, 23, 34, 45, 64, 67, 81])

if __name__ == "__main__":
	unittest.main()