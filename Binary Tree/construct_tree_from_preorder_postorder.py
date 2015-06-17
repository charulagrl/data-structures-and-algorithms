# -*- coding: UTF-8 -*-

# Construct tree from its preorder and postorder traversal

import binary_tree

class Node(object):

	def __init__(self, data):

		self.data = data
		self.left = None
		self.right = None

index_pre = 0
def construct_tree(preorder, postorder, st_in, end_in):
	global index_pre

	if index_pre >= len(preorder) or st_in > end_in:
		return

	else:
		root = Node(preorder[index_pre])
		index_pre += 1

		if st_in == end_in:
			return root

		index = postorder.index(preorder[index_pre])

		if index <= len(postorder):
			root.left = construct_tree(preorder, postorder, st_in, index)

			root.right = construct_tree(preorder, postorder, index+1, end_in-1)

	return root

preorder = [1, 2, 4, 8, 9, 5, 3, 6, 7]
postorder = [8, 9, 4, 5, 2, 6, 7, 3, 1]

root = construct_tree(preorder, postorder, 0, len(postorder)-1)
print "Inorder traversal of constructed tree"
tree = binary_tree.Tree(root)
tree.inorder(root)