# -*- coding: UTF-8 -*-

# Check if a given tree is a sumTree i.e. A SumTree is a Binary Tree where the value of a node is equal to sum of the nodes present in its left subtree and right subtree. 

import binary_tree

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

			if root.data == (ls+rs):
				return True

		return False


tree = binary_tree.construct_binary_tree()
tree.inorder(tree.root)
print check_sumtree(tree.root)