# -*- coding: UTF-8 -*-

# Matrix chain multiplication
import sys

# Recursive implementation
def matrix(arr, i, j):

	min_count = sys.maxint
	if i == j:
		return 0

	for k in range(i, j):

		count = matrix(arr, i, k) + matrix(arr, k+1, j) + arr[i-1]*arr[k]*arr[j]

		if count < min_count:
			min_count = count

	return min_count


# DP implementation
def matric_dynamic(arr):
	n = len(arr)

	mat = []
	# initialize n * n matrix with None
	for i in range(n):
		mat.append([None]*n)

	# Cost would be zero when multiplying one matrix
	for i in range(n):
		mat[i][i] = 0

	# Considering all the possible chain lengths
	for L in range(2, n):
		for i in range(n-L+1):
			j = i+L-1
			mat[i][j] = sys.maxint
			for k in range(i, j):
				res = mat[i][k] + mat[k+1][j] + arr[i-1] * arr[k] * arr[j]

				if res < mat[i][j]:
					mat[i][j] = res

	return mat[1][n-1]

	
arr = [40, 20, 30, 10, 30]
min_count = matrix(arr, 1, len(arr)-1)
print min_count
print "Solving by dynammic programming"
print matric_dynamic(arr)
