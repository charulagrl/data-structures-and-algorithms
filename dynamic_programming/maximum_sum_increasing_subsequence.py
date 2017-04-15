# -*- coding: UTF-8 -*-

# Maximum Sum Increasing subsequence

maximum_s = -10000000

# Recursive implementation
def maximum_sum(arr, index):

	global maximum_s
	if index == 1:
		return arr[index-1]

	else:
		max_value = -100000000

		for i in range(1, index):
			res = maximum_sum(arr, i)

			if arr[index-1] > arr[i-1] and res + arr[index-1] > max_value:
				max_value = res + arr[index-1]

		if max_value > maximum_s:
			maximum_s = max_value

		return max_value


def maximum_sum_dynamic(arr):
	soln = [None] * len(arr)

	for i in range(len(arr)):
		soln[i] = arr[i]

	for i in range(1, len(arr)):
		for j in range(i):
			if arr[j] < arr[i] and soln[j] + arr[i] > soln[i]:
				soln[i] = soln[j] + arr[i]


	print max(soln)

arr = [1, 101, 2, 3, 100, 4, 5]
maximum_sum(arr, len(arr))
print maximum_s
print "Solving by DP"
maximum_sum_dynamic(arr)

