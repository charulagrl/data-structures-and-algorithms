# -*- coding: UTF-8 -*-

# Cutting a rod

'''
	Given a rod of length n inches and an array of prices that contains prices of all pieces of size smaller than n.
	Determine the maximum value obtainable by cutting up the rod and selling the pieces.
'''
import sys


def cutting_a_rod(length, values):
	'''Recursive implementation to find the maximum values obtained by cutting a rod'''
	# If length is less than or equal to 0
	if length <= 0:
		return 0

	else:
		max_val = -sys.maxint
		for i in range(length):
			# Cut the rod at different lengths
			# length-i-1 because at index 0, length is 1
			max_val = max(values[i] + cutting_a_rod(length-i-1, values), max_val)

	return max_val


def cutting_a_rod_dynamic(values, length):
	'''Dynamic Programming implementation to find the maximum values obtained by cutting a rod'''
	soln = [0] * (length+1)

	for i in range(1, length+1):
		soln[i] = -sys.maxint
		for j in range(i):
			res = soln[i-j-1] + values[j]
			if res > soln[i]:
				soln[i] = res

	return soln[length]

def cut_a_rod(index, price, length):
	if not length or not price:
		return 0

	if length < index:
		return cut_a_rod(index+1, price[1:], length)

	else:
		return max(cut_a_rod(index, price, length-index) + price[0], cut_a_rod(index+1, price[1:], length))

def cut_a_rod_dynamic(price, length):
	cost = [[0] * (length+1) for i in range(length+1)]

	for i in range(length+1):
		for j in range(length):
			if not i or not j:
				cost[i][j] = 0
			elif i > j:
				cost[i][j] = max(cost[i-j-1][j] + price[j-1], cost[i][j])
			else:
				cost[i][j] = cost[i][j-1]

		print cost
	return cost[length][length]


import unittest

class MyTest(unittest.TestCase):
	def setUp(self):
		self.price = [1, 5, 8, 9]
		self.length = len(self.price)

	def test_cutting_a_rod(self):
		self.assertEqual(cutting_a_rod(self.length, self.price), 10)

	def test_cuttin_a_rod_dynamic(self):
		self.assertEqual(cutting_a_rod_dynamic(self.price, self.length), 10)

	def test_cut_a_rod_recursive(self):
		self.assertEqual(cut_a_rod(1, self.price, self.length), 10)

	def test_cut_a_rod_dynamic(self):
		self.assertEqual(cut_a_rod_dynamic(self.price, self.length), 10)

if __name__ == "__main__":
	unittest.main()

