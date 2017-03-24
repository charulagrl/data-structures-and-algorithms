# -*- coding: UTF-8 -*-

# Longest common subsequence

# Recursive solution
def LCS(arr, arr2, m, n):

	if m == 0 or n == 0:
		return 0

	if arr[m-1] == arr2[n-1]:
		return LCS(arr, arr2, m-1, n-1) + 1

	else:
		return max(LCS(arr, arr2, m-1, n), LCS(arr, arr2, m, n-1))

# Dynamic PRogramming solution
def LCS_dynamic(arr, arr2, m, n):
	soln = []
	for i in range(m+1):
		soln.append([0]*(n+1))

	for i in range(m+1):
		soln[i][0] = 0

	for j in range(n+1):
		soln[0][j] = 0

	for i in range(1, m+1):
		for j in range(1, n+1):
			if arr[i-1] == arr2[j-1]:
				soln[i][j] = soln[i-1][j-1] + 1
			else:
				soln[i][j] = max(soln[i-1][j], soln[i][j-1])

	return soln[m][n]

str1 = "AGGTAB"
str2 = "GXTXAYB"
print LCS(str1, str2, len(str1), len(str2))
print "Dynamic programming soln"
print LCS_dynamic(str1, str2, len(str1), len(str2))
