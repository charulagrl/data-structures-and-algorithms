# -*- coding: UTF-8 -*-

# N Queen Problem
def is_safe(n, row, col):
	for i in range(col):
		if n[row][i]:
			return False

	# check for rows on left side
	for j in range(row):
		if n[j][col]:
			return False

	# check for upper right diagonal
	i = row
	j = col
	while i < len(n) and j >=0:
		if n[i][j]:
			return False
		i += 1
		j -= 1

	# check for upper left diagonal
	i = row
	j = col
	while i >= 0 and j >= 0:
		if n[i][j]:
			return False
		i -= 1
		j -= 1

	return True


def n_queen(size, n, col):

	if col >= size:
		return True

	else:
		for row in range(size):
			if is_safe(n, row, col):
				n[row][col] = 1
				# recursively check for further columns
				if n_queen(size, n, col+1):
					return True
				# Backtarck
				n[row][col] = 0

		return False

size = 4
# initialize board with all 0's
n = []
for i in range(size):
	n.append([0]*size)

if not n_queen(size, n, 0):
	print "Solution does not exist"
else:
	print "Following solution exists for size %s" %str(size)
	print n