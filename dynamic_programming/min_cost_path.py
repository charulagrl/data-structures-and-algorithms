# -*- coding: UTF-8 -*-

# Program to find minimum cost path
import sys

# Recursive approach to solve minimum cost path problem
def min_cost(cell, i, j):
	if i < 0 or j < 0:
		return sys.maxint

	if i == 0 and j == 0:
		return cell[i][j]
	
	else:
		min_left = min_cost(cell, i-1, j)
		min_top = min_cost(cell, i, j-1)
		min_diagonal = min_cost(cell, i-1, j-1)

		return min(min_left, min(min_top, min_diagonal)) + cell[i][j]

# Dynamic Programming approach to minimum cost path problem
def min_cost_dp(cell, i, j):

	for i in range(len(cell)):
		for j in range(len(cell[0])):
			if i > 0 or j > 0:
				min_left = cell[i-1][j] if i-1 >=0 else sys.maxint
				min_top = cell[i][j-1] if j-1 >=0 else sys.maxint
				min_diagonal = cell[i-1][j-1] if j-1 >=0 and i-1 >=0 else sys.maxint

				cell[i][j] += min(min_left, min(min_top, min_diagonal))

cell = [[1, 2, 3],
				[4, 8, 2],
				[1, 5, 3]]

min_cost_dp(cell, 2, 2)
print cell[2][2]
