# -*- coding: UTF-8 -*-

# Knights tour problem

def isSafe(board, x, y, count):
	if x < 0 or x >= len(board) or y < 0 or y >= len(board):
		return False

	if board[x][y] != -1:
		return False

	return True

def Knights_Tour(board, curr_x, curr_y, count, max_count):
	x_moves = [-2, -2, -1, -1, 1, 1, 2, 2]
	y_moves = [-1, 1, -2, 2, -2, 2, -1, 1]

	if count == max_count:
		return True
	else:
		for i in range(len(x_moves)):
			next_x = curr_x + x_moves[i]
			next_y = curr_y + y_moves[i]
			if isSafe(board, next_x, next_y, count):
				board[next_x][next_y] = count

				if Knights_Tour(board, next_x, next_y, count+1, max_count):
					return True

				board[next_x][next_y] = -1

	return False

if __name__=="__main__":
	board = []
	N = 8

	for i in range(N):
		board.append([-1]*N)

	board[0][0] = 0
	count = 0
	max_count = len(board)*len(board)

	if Knights_Tour(board, 0, 0, count+1, max_count):
		for i in board:
			print i
	else:
		print "Solution does not exist"
