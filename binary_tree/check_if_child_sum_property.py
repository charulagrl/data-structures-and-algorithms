# -*- coding: UTF-8 -*-

# Program to check if child sum property holds in the binary tree

import binary_tree

def check_child_sum(root):

	if root is None or (root.left is None and root.right is None):
		return True

	else:
		sum = 0

		if root.left:
			sum += root.left.data

		if root.right:
			sum += root.right.data

		if sum == root.data and check_child_sum(root.left) and check_child_sum(root.right):
			return True
		else:
			return False

if __name__=="__main__":
	tree = binary_tree.construct_binary_tree()

	print check_child_sum(tree.root)