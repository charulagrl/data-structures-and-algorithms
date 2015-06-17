# -*- coding: UTF-8 -*-

# Program to convert tree to sumTree
import binary_tree

def increment(root, value):
	if root.left:
		root.left.data += value
		increment(root.left, value)
	elif root.right:
		root.right.data += value
		increment(root.right, value)

def convert_to_SumTree(root):
	if root is None:
		return 0

	old_value = root.data
	root.data = convert_to_SumTree(root.left) + convert_to_SumTree(root.right)

	return root.data+old_value

tree = binary_tree.construct_binary_tree()
convert_to_SumTree(tree.root)
tree.inorder(tree.root)