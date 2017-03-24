# -*- coding: UTF-8 -*-

# Edit distance 

# Given two strings of size m, n and set of operations replace (R), insert (I) and delete (D) all at equal cost. Find minimum number of edits (operations) required to convert one string into another.

# Recursive solution

def edit_distance(str1, str2, m, n):

	if m == 0 or n == 0:
		return 0

	if m == 0:
		return n

	if n == 0:
		return m

	upper_corner = edit_distance(str1, str2, m-1, n-1) + (str1[m-1] != str2[n-1])
	left = edit_distance(str1, str2, m, n-1) + 1
	down = edit_distance(str1, str2, m-1, n) + 1

	return min(upper_corner, min(left, down))

def edit_distance_dynamic(str1, str2, m, n):

	soln = []
	for i in range(m+1):
		soln.append([0]*(n+1))

	for i in range(m+1):
		soln[i][0] = i

	for j in range(n+1):
		soln[0][j] = j

	for i in range(1, m+1):
		for j in range(1, n+1):
			corner = soln[i-1][j-1] + (str1[i-1] != str2[j-1])
			left = soln[i][j-1] + 1
			down = soln[i-1][j] + 1

			soln[i][j] = min(corner, min(left, down))

	return soln[m][n]

str1 = "SUNR"
str2 = "SUNUE"
print edit_distance(str1, str2, len(str1), len(str2))
print "Dynamic Programmin Solution"
print edit_distance_dynamic(str1, str2, len(str1), len(str2))
