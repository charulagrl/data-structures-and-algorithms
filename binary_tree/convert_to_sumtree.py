# -*- coding: UTF-8 -*-

# Program to convert tree to sumTree
import binary_tree

def convert_to_SumTree(root):
	if root is None:
		return 0

	old_value = root.data
	root.data = convert_to_SumTree(root.left) + convert_to_SumTree(root.right)

	return root.data+old_value

def check_sumtree(root):
	if not root or (not root.left and not root.right):
		return True

	else:

		if check_sumtree(root.left) and check_sumtree(root.right):

			if not root.left:
				ls = 0
			elif not root.left.left and not root.left.right:
				ls = root.left.data
			else:
				ls = 2 * root.left.data

			if not root.right:
				rs = 0
			elif not root.right.left and not root.right.right:
				rs = root.right.data
			else:
				rs = 2 * root.right.data

			if root.data != (ls+rs):
				root.data = ls+rs

tree = binary_tree.construct_binary_tree()
convert_to_SumTree(tree.root)
tree.inorder(tree.root)
check_sumtree(tree.root)
tree.inorder(tree.root)