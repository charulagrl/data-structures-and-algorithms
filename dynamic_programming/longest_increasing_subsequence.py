# -*- coding: UTF-8 -*-

# Program to find longest increasing subsequence (LIS)

import sys
max_lis_length = -sys.maxint

def longest_increasing_subsequence(array, length):
	'''Recursive implementation to find the length of longest increasing subsequence'''
	global max_lis_length

	# If the array contains only one element, lis will be 1
	if length == 1:
		return 1

	current_lis_length = 1
	
	for i in range(1, length):
		''' Find the length od lis for sub array till index i'''
		subproblem_lis_length = longest_increasing_subsequence(array, i)

		if (array[i-1] < array[length-1] and current_lis_length < subproblem_lis_length + 1):
			current_lis_length = subproblem_lis_length + 1

	if current_lis_length > max_lis_length:
		max_lis_length = current_lis_length

	return current_lis_length

def longest_increasing_subsequence_dynamic(array, length):
	'''Using dynamic programming to find the length of longest increasing subsequence'''
	lis = [1] * length

	for i in range(length):
		for j in range(i):
			if (array[j] < array[i] and lis[i] < lis[j] + 1):
				lis[i] = lis[j] + 1
	
	return max(lis)

import unittest

class MyTest(unittest.TestCase):
	def setUp(self):
		self.array = [10, 22, 9, 33, 21, 50, 41, 60, 80]
		self.length = len(self.array)

	def test_longest_increasing_subsequence(self):
		self.assertEqual(longest_increasing_subsequence(self.array, self.length), 6)

	def test_longest_increasing_subsequence_dynamic(self):
		self.assertEqual(longest_increasing_subsequence_dynamic(self.array, self.length), 6)

if __name__ == "__main__":
	unittest.main()
