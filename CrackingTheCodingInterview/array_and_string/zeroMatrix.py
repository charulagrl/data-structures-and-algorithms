'''
	Problem: Write an algorithm such that if an element in an M * N matrix is zeo, its entire row and column is set to 0

	Solution: Loop over the matrix and look for element who's value is 0. Take two arrays whose length is equal to 
	number of rows and columns respectively. If any element is zero mark that value of row and column in each array as true. 

	Time Complexity: O(M * N)
	Space Complexity: O(M + N)

'''

def zeroMatrix(matrix):

	row_len = len(matrix)
	col_len = len(matrix[0])

	# Will store True if the row contains any zero
	row_array = [False] * row_len
	# Will store True if the column contains any zero
	col_array = [False] * col_len

	# store the row and column index with value 0
	for i in range(row_len):
		for j in range(col_len):

			if matrix[i][j] == 0:
				row_array[i] = True
				col_array[j] = True

	# Check for each row and make the entire row zero if found True
	for i in range(row_len):

		if row_array[i]:
			# nullify row
			for j in range(col_len):
				matrix[i][j] = 0

	# If any zero found for a column, make the entire column zero
	for i in range(col_len):

		if col_array[i]:
			# nullify column
			for j in range(row_len):
				matrix[j][i] = 0


	return matrix

# Writing unit-test for the above function
import unittest

class MyTest(unittest.TestCase):

	def test(self):
		self.assertEqual(zeroMatrix([[1, 2, 3], [4, 5, 6], [7, 8, 0]]), [[1, 2, 0], [4, 5, 0], [0, 0, 0]])

unittest.main()
