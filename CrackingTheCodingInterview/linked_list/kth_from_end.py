# -*- coding: UTF-8 -*-

'''
	Problem: Implement a program to print kth element from end

	example: 1 -> 4 -> 8 -> 9 -> 2       k=3
	answer: 8

	Approach: Take a pointer and iterate it through the kthe index in the list. Then start a counter from head and iterate
	both the counters till the first counter reaches end of the list. Then return the second pointer. 

	Time Complexity: O(n)

'''

def k_from_end(head, k):

	if not head:
		raise ValueError("List is empty")

	k_node = head
	counter = 0

	while(counter < k):
		k_node = k_node.nextnode

		if not k_node.nextnode:
			raise ValueError("kth index out of range")

		counter += 1

	current = head
	while (k_node):
		current = current.nextnode
		k_node = k_node.nextnode


	return current.data
