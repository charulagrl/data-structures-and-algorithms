# -*- coding: UTF-8 -*-

'''
	Problem: Implement a program to remove duplicates elements from a linked list
	
	Example: 2 -> 1 -> 7 -> 2 -> 9 -> 1 -> 8 
	Result: 2 -> 1 -> 7 -> 9 -> 8

	Approach 1: Iterate through each element in a linked list and look for the same element in the list ahead. 
	If found, delete that element. 

	Time Complexity: O(n * n)

	Approach 2: Store the elements in a hash-map and if next time the same element is encountered, delete it. 

	Time Complexity: O(n) Space Complexity: O(n)
'''
def remove_duplicates(head):
	hash_map = {}
	current = head
	prev = None

	while (current):
		if current.data in hash_map:
			prev.nextnode = current.nextnode

		else:
			hash_map[current.data] = 1

		prev = current
		current = current.nextnode
