# -*- coding: UTF-8 -*-

# Construct a complete binary tree from its linked list representation

import binary_tree

class Node(object):
	def __init__(self, data):
		self.data = data
		self.next = None

def get_value_at_index(head, i):
	if head is None:
		return

	count = 0
	while count < i and head:
		count += 1
		head = head.next

	if head:
		return head.data
	else:
		return None

def construct_tree(head, i):

	if head is None:
		return

	value = get_value_at_index(head, i)

	if not value:
		return

	root = binary_tree.Node(value)

	root.left = construct_tree(head, 2*i+1)
	root.right = construct_tree(head, 2*i+2)

	return root

# Create a linked list
head = Node(10)
head.next = Node(12)
head.next.next = Node(15)
head.next.next.next = Node(25)
head.next.next.next.next = Node(30)
head.next.next.next.next.next = Node(36)

root = construct_tree(head, 0)
tree = binary_tree.Tree(root)
tree.inorder(tree.root)