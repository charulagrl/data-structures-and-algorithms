# -*- coding: UTF-8 -*-

# Minimum number of jumps to reach end

import sys

# Recursive approach
def min_jump(arr, start, end):
	if start == end:
		return 0

	if arr[start] == 0:
		return sys.maxint

	minimum = sys.maxint
	i = start+1
	while i <= start+arr[start] and  i <= end:
		res = min_jump(arr, i, end)
		if res != sys.maxint and res + 1 < minimum:
			minimum = res + 1

		i+=1

	return minimum

# Dynamic Programmic implementation
def min_jump_dynamic(arr):
	n = len(arr)

	if n == 0 or arr[0] == 0:
		return sys.maxint

	soln = [0] * n

	for i in range(1, n):
		soln[i] = sys.maxint
		for j in range(i):
				if i <= j + arr[j] and soln[j] != sys.maxint:
					soln[i] = min(soln[i], soln[j]+1)
					break

	return soln[n-1]

arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
print min_jump(arr, 0, len(arr)-1)
print min_jump_dynamic(arr)