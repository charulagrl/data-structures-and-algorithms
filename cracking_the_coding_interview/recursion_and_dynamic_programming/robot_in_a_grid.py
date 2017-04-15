# -*- coding: UTF-8 -*-

# def find_path(cur_i, cur_j, grid, R, C):
# 	if 0 <= cur_i < R and 0 <= cur_j < C:
# 		grid[cur_i][cur_j] = "P"

# 	print grid, cur_i, cur_j
# 	if grid[R-1][C-1] == "P":
# 		return grid

# 	if cur_j < C-1 and grid[cur_i][cur_j+1] not in ['X', 'P']:
# 		print "recurse", cur_j+1
# 		find_path(cur_i, cur_j+1, grid, R, C)

# 	if cur_i < R-1 and grid[cur_i+1][cur_j] not in ['X', 'P']:
# 		print "recurse row", cur_i+1
# 		find_path(cur_i+1, cur_j, grid, R, C)

def find_path(cur_i, cur_j, grid):

	if cur_i == 0 and cur_j == 0:
		return grid

	grid[cur_i][cur_j] = "P"

	print grid
	if cur_j > 0 and grid[cur_i][cur_j-1] not in ['X', 'P']:
		print "recurse col", cur_j-1
		find_path(cur_i, cur_j-1, grid)

	if cur_i > 0 and grid[cur_i-1][cur_j] not in ['X', 'P']:
		print "recurse row", cur_i-1
		find_path(cur_i-1, cur_j, grid)

if __name__ == "__main__":
	grid = []
	for i in range(6):
		grid.append(['N']*5)
	
	grid[0][2] = "X"
	grid[1][4] = "X"
	grid[2][3] = "X"
	grid[4][0] = "X"
	print grid
	
	find_path(len(grid)-1, len(grid[0])-1, grid)
	print grid