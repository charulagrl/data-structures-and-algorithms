# -*- coding: UTF-8 -*-

# Program to construct binary tree from its inorder and preorder traversal

import binary_tree

pre_index = 0

def search(inorder, data):
	if data in inorder:
		return inorder.index(data)
	else:
		raise ValueError("Data not present in inorder list")

def construct_tree(inorder, preorder, s_in, e_in):
	global pre_index

	if s_in > e_in:
		return

	root = binary_tree.Node(preorder[pre_index])

	pre_index += 1

	ind = search(inorder, root.data)

	root.left = construct_tree(inorder, preorder, s_in, ind-1)
	root.right = construct_tree(inorder, preorder, ind+1, e_in)

	return root

if __name__=="__main__":

	root = construct_tree([4, 2, 5, 1, 3], [1, 2, 4, 5, 3], 0, 4)

	tree = binary_tree.Tree(root)

	tree.inorder(root)
