# -*- coding: UTF-8 -*-

'''

   Problem: Implement an algorithm to determine if a string has all unique characters. 

'''
   

'''
   Naive Approach: Loop through each character in the string and check in the entire string if that character is present. 
   If even one such character found, 
   return False.

   Time complexity: O(n*2) where n is the length of the string.    

'''
def is_unique(s):

   length = len(s)

   for a in range(length):
      for b in range(a+1, length):
         if s[a] == s[b]:
            return False

   # When string has all unique characters
   return True

'''
   Approach 2: Sort the string first and loop over the string and compare each character with its next character, if 
   there is one such character, it returns false. 

   Time complexity: Sorting O(n*logn) and looping over string O(n). So the complexity will come down to O(n*logn)
'''

def check_is_unique(s):

   # Calling inbuilt sort function in Python
   s = sorted(s)

   length = len(s)
   for i in range(length-1):
      for j in range(i+1, length):
         # Comparing each element with its next element
         if s[i] == s[j]:
            return False

   return True


'''
   Approach 3: Store each character in a hash_map with key as each character and if any character is already found in 
   hash_map return false.

   Time complexity: O(n) to loop over string
   Space Complexity: O(n) to store n characters 

'''
def unique_character_string(s):

	# Declaring hash_map using python dictionaries
	hash_map = {}

	for i in s:
		if i in hash_map:
			return False
		else:
			hash_map[i] = True

	return True
