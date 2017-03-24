# -*- coding: UTF-8 -*- 

'''

	Problem: An image is represented by N*N matrix, where each pixel is four bytes. Write a method to rotate matrix by 90 degrees.

	example:
		1   2   3   4                               13  9   5  1
		5   6   7   8                 --->          14  10  6  2
		9   10  11  12                              15  11  7  3
		13  14  15  16                              16  12  8  4

'''

def rotate(matrix):

	N = len(matrix)
	temp_array = [0]* N

	for i in range(len(N/2)):
		for j in range(N):
			temp_array = matrix[i][j]
			matrix[i][j] = matrix[N-i-1][j]
			matrix[N-i-1][j] = matrix[N-i-1][N-j-1]
			matrix[N-i-1][N-j-1] = matrix[i][N-j-1]
			matrix[i][N-j-1] = temp_array
