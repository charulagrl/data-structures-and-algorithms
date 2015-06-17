# -*- coding: UTF-8 -*-

# Binomial Coefficient (Dynammic Programming)

# Recursive solution
def binomial_coefficient(n, k):

	if k == 0 or k == n:
		return 1

	return binomial_coefficient(n-1, k-1) + binomial_coefficient(n-1, k)

# Dynammic Programming
def binomial_coefficient_dynamic(n, k):
	soln = []
	for i in range(n+1):
		soln.append([0]*(k+1))

	for i in range(n+1):
		for j in range(k+1):

			if j == 0 or j == n:
				soln[i][j] = 1

			else:
				soln[i][j] = soln[i-1][j-1] + soln[i-1][j]

	return soln[n][k]

n = 5
k = 2
print binomial_coefficient(n,k)
print "Solving by DP"
print binomial_coefficient_dynamic(n, k)