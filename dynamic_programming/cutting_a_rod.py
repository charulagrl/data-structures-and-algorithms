# -*- coding: UTF-8 -*-

# Cutting a rod

# Recursive implementation
def cutting_a_rod(l, values):
	if l <= 0:
		return 0

	else:
		max_val = -111111111
		for i in range(l):
			max_val = max(values[i] + cutting_a_rod(l-i-1, values), max_val)

	return max_val

# Dynamic Programming implementation
def cutting_a_rod_dynamic(values):

	soln = [0] * (len(values)+1)

	soln[0] = 0

	for i in range(1, len(values)+1):
		soln[i] = -11111
		for j in range(i):
			res = soln[i-j-1] + values[j]
			if res > soln[i]:
				soln[i] = res

	return soln[len(values)]

arr = [1, 5, 8, 9, 10, 17, 17, 20]
print cutting_a_rod(len(arr), arr)
print cutting_a_rod_dynamic(arr)
