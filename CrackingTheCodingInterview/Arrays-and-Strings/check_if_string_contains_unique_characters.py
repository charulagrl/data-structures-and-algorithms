# -*- coding: UTF-8 -*-

'''

   Problem: Implement an algorithm to determine if a string has all unique characters. 

   Naive Approach: Loop through each character in the string and check in the entire string if that character is present. 
   If even one such character found, 
   return False.

   Time complexity: O(n*2) where n is the length of the string. 

   Approach 2: Sort the string first and loop over the string and compare each character with its next character, if 
   there is one such character, it returns false. 

   Time complexity: Sorting O(n*logn) and Looping over string O(n). So the complexity will come down to O(n*logn)

   Approach 3: Store each character in a hash_map with key as each character and if any character is already found in 
   hash_map return false.

   Time complexity: O(n) to loop over string
   Space Complexity: O(n) to store n characters 

'''

# Check if string has unique characters using hash map
def unique_character_string(s):

	# Declaring hash_map using python dictionaries
	hash_map = {}

	for i in s:

		if i in hash_map:
			return False
		else:
			hash_map[i] = True

	return True
