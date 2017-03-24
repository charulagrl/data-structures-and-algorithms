# -*- coding: UTF-8 -*-

# Program to solve coin change problem

# Recursive implementation
def coin_change(N, S):
	
	if N == 0:
		return 1

	if N < 0:
		return 0

	if len(S) <= 0 and N >= 1:
		return 0

	else:
		return coin_change(N-S[-1], S) + coin_change(N, S[0:-1])



# Dynamic Programming Solution
def coin_change_dp(N, S):
	soln = []
	for i in range(N+1):
		soln.append([0]*len(S))

	for i in range(len(S)):
		soln[0][i] = 1

	for i in range(1, N+1):
		for j in range(0, len(S)):
			x = soln[i - S[j]][j] if i-S[j] >= 0 else 0
			y = soln[i][j-1] if j>=1 else 0

			soln[i][j] = x+y

	return soln[N][len(S)-1]

N = 4
S = [1, 2, 3]

count = coin_change_dp(N, S)
print count