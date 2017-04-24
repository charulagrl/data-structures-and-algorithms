# coding: UTF-8

'''
	Binary Search is a searching algorithm that is very efficient and most commonly used techniques used in solving problems. 

	Binary search divides the problem into half at each iteration. It works on a sorted set, and the number of iterations can
	always be reduced on the basis of value that is being searched. 

	Complexity: O(log n)


'''

def binary_search(low, high, array, key):
	''' Search for the key and return the index of the key.
		If not found, returns -1'''
	while(low <= high):
		mid = (low + high) / 2

		if array[mid] == key:
			return mid

		elif array[mid] > key:
			low = mid + 1

		elif array[mid] < key:
			high = mid - 1


	return -1


# Writing unit-test for the above function
import unittest

class MyTest(unittest.TestCase):
	def setUp(self):
		self.array = [2, 5, 6, 12, 17, 23, 34, 45, 67, 81]
		self.high = len(self.array)
		self.key = 23

	def test(self):
		self.assertEqual(binary_search(0, self.high, self.array, self.key), 5)

if __name__ == "__main__":
	unittest.main()