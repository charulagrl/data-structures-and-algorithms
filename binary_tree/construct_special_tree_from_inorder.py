# -*- coding: UTF-8 -*-

# Given Inorder Traversal of a Special Binary Tree in which key of every node is greater than keys in left and right children, construct the Binary Tree and return root.

import binary_tree

def find_max(inorder, st_in, end_in):
	max = st_in
	for i in range(st_in+1, end_in+1):
		if inorder[i] > inorder[max]:
			max = i

	return max

def construct_tree(inorder, st_in, end_in):

	if st_in > end_in:
		return

	max_ind = find_max(inorder, st_in, end_in)
	root = binary_tree.Node(inorder[max_ind])

	if st_in == end_in:
		return root

	root.left = construct_tree(inorder, st_in, max_ind-1)
	root.right = construct_tree(inorder, max_ind+1, end_in)

	return root

inorder = [1, 5, 10, 40, 30, 15, 28, 20]

root = construct_tree(inorder, 0, len(inorder)-1)

tree = binary_tree.Tree(root)
tree.inorder(tree.root)