# -*- coding: UTF-8 -*-

# Longest Palindromic subsequence

# Recursive implementation
def LPS(str1, i, j):
	if i == j:
		return 1

	if str1[i] == str1[j] and i+1 == j:
		return 2

	if str1[i] == str1[j]:
		return 2 + LPS(str1, i+1, j-1)

	else:
		return max(LPS(str1, i, j-1), LPS(str1, i+1, j))

# Dynamic Programming implementation
def LPS_dynamic(str1):
	soln = []

	for i in range(len(str1)):
		soln.append([0]*len(str1))


	# When length of string is 1
	for i in range(len(str1)):
		soln[i][i] = 1

	for i in range(2, len(str1)+1):
		for j in range(len(str1)-i+1):
			k = i+j-1
			if str1[j] == str1[k] and i == 2:
				soln[j][k] = 2
			if str1[j] == str1[k]:
				soln[j][k] = 2 + soln[j+1][k-1]
			else:
				soln[j][k] = max(soln[j+1][k], soln[j][k-1])

	return soln[0][len(str1)-1]

s = "BBAAB"
print LPS(s, 0, len(s)-1)
print LPS_dynamic(s)