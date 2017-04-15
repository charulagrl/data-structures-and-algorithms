# -*- coding: UTF-8 -*-

# Egg dropping puzzle

import sys

# Recursive implementation
def egg_dropping_puzzle(n, k):

	if k == 0 or k == 1:
		return k
	if n == 1:
		return k

	min_value = sys.maxint

	for i in range(2, k+1):
		res = max(egg_dropping_puzzle(n-1, i-1), egg_dropping_puzzle(n, k-i))

		if res < min_value:
			min_value = res

	return min_value + 1

# Dynamic Programming implementation
def egg_dropping_puzzle_dynamic(n, k):

	soln = []

	for i in range(n+1):
		soln.append([None]*(k+1))

	# initializing for the case when floor is 0 or floor is one
	for i in range(n+1):
		soln[i][0] = 0
		soln[i][1] = 1

	# initializing for the case when ball is one
	for j in range(1, k+1):
		soln[1][j] = j

	for i in range(2, n+1):
		for j in range(2, k+1):
			soln[i][j] = sys.maxint
			for x in range(1, j+1):
				res = max(soln[i-1][x-1], soln[i][j-x]) + 1
				if res < soln[i][j]:
					soln[i][j] = res

	return soln[n][k]

n = 2
k = 10
print egg_dropping_puzzle(n, k)
print egg_dropping_puzzle_dynamic(n, k)