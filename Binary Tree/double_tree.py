# -*- coding: UTF-8 -*-

# Program to print double tree of a tree

import binary_tree

def double_tree(root):
	if root is None:
		return
	else:

		double_tree(root.left)
		double_tree(root.right)

		temp = root.left
		root.left = binary_tree.Node(root.data)
		root.left.left = temp

	return root

tree = binary_tree.construct_binary_tree()

tree.inorder(tree.root)

print "Conversion to double tree"
tree.root = double_tree(tree.root)

tree.inorder(tree.root)