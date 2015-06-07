# -*- coding: UTF-8 -*-

# Program to print kth node from end

import initialize

def k_from_end(head, k):

	if head is None:
		return

	node_ptr = head
	main_ptr = head

	count = 0

	while (count < k):
		node_ptr = node_ptr.nextnode
		count += 1

	while (node_ptr):
		main_ptr = main_ptr.nextnode
		node_ptr = node_ptr.nextnode

	print main_ptr.data

lList = initialize.initialize_linked_list()

k_from_end(lList.head, 5)