# -*- coding: UTF-8 -*-

'''
	Problem: Implement an algorithm to delete node in the middle of a singly linked list, given only access to that node. 

	Solution: When you are given the pointer to the node, change the value to the next pointer value and 
	next pointer to the next of next pointer. 
'''

import linked_list

def delete_middle_node(node):
	''' Function to delete a node in between the linked list.'''
	if (node == None or node.nextnode == None):
		return False

	next = node.nextnode
	node.data = next.data
	node.nextnode = next.nextnode

	return True

def delete_middle_helper():
	''' Function to initialize linked list and call delete middle node function'''
	llist = linked_list.initialize_linked_list()
	k = delete_middle_node(llist.head.nextnode)
	print ""
	llist.print_list()
