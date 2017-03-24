# -*- coding: UTF-8 -*-

'''

	Problem: Program to check if one word is a substring of another. If you have two strings s1 and s2, write code to check 
	if s2 is a rotation of s1 using only one call to isSubstring. 

	example: hoolahoop is a rotation of "lahoophoo"

	Naive approach: Rotate the first string clockwise and anitclockwise by each letter and compare with the second string. If 
	at any point the two strings are same, then it is a rotation of each other.

	Time Complexity: O(n+n) number of rotations. For each rotation, there will be comparison among strings and contenation of 
	two strings. 

	Solution: Add the second string to the same string and then find the first string in the second string. If you can find it,
	then it is a substring otherwise not. The criteria is s1 is always a substring of s2s2.

	Time Complexity: O(n) where n is the length of the string.  

'''


def isSubstring(s1, s2):

	s2s2 = s2 + s2

	# in checks if one string is part of another.
	if s1 in s2s2:
		return True

	else:
		return False
