# -*- coding: UTF-8 -*-

# Program to find level of a node in a binary tree

import binary_tree

def level_of_node(root, node, level):
	if root is None:
		return

	if root.data == node:
		print level

	level_of_node(root.left, node, level+1)
	level_of_node(root.right, node, level+1)

tree = binary_tree.construct_binary_tree()

level_of_node(tree.root, 5, 0)