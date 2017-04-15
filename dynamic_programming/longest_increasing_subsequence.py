# -*- coding: UTF-8 -*-

# Program to find longest increasing subsequence (LIS)


max_length = 1

# Recursive solution
def LIS(arr, n):

	global max_length
	if n == 1:
		return 1

	max_ending_here = 1
	for i in range(1, n):
		res = LIS(arr, i)
		if arr[i-1] < arr[n-1] and res+1 > max_ending_here:
			max_ending_here = res+1

	if max_ending_here > max_length:
		max_length = max_ending_here

	return max_ending_here

# Dynamic Programming solution
def LIS_dynamic(arr):
	n = len(arr)

	lis = [1] * n

	for i in range(1, n):
		for j in range(i):
			if arr[j] < arr[i] and lis[j] + 1 > lis[i]:
				lis[i] = lis[j] + 1

	return max(lis)


l = [10, 22, 9, 33, 21, 50, 41, 60, 80]

LIS(l, len(l))
print "Solving through dynammic programming"
print LIS_dynamic(l)
print "Solving through recursive way"
print max_length

