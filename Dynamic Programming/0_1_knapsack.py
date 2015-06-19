# -*- coding: UTF-8 -*-

# Program to find solution to 0-1 Knapsack Problem

# recursive solution to solve 0-1 knapsack problem
# Time complexity : O(2^n)

def knapsack(W, values, weights, n):
	if n == 0 or W == 0:
		return 0

	if weights[n-1] > W:
		return knapsack(W, values, weights, n-1)

	else:

		return max(values[n-1] + knapsack(W-weights[n-1], values, weights, n-1), knapsack(W, values, weights, n-1))

# Dynamic programming implementation of knapsack problem
# time-complexity : O(W*n)

def knapsack_dynamic(W, values, weights, n):

	K = []

	for i in range(n+1):
		K.append([0]*(W+1))

	for i in range(n+1):
		for w in range(W+1):
			if i == 0 or w == 0:
				K[i][w] = 0
			elif weights[i-1] <= w:
				K[i][w] = max(values[i-1]+K[i-1][w-weights[i-1]]
					, K[i-1][w])
			else:
				K[i][w] = K[i-1][w]

	return K[n][W]

if __name__=="__main__":
	values = [60, 100, 120]
	weights = [10, 20, 30]
	W = 50

	print knapsack(W, values, weights, 3)
	print knapsack_dynamic(W, values, weights, 3)