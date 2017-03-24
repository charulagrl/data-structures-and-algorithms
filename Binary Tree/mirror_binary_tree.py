# -*- coding: UTF-8 -*-

# Program to find mirror of a binary tree

import binary_tree

def mirror(root):
	if root is None or (root.left is None and root.right is None):
		return

	else:

		mirror(root.left)
		mirror(root.right)

		temp = root.left
		root.left = root.right
		root.right = temp

if __name__=="__main__":
	tree = binary_tree.construct_binary_tree()

	mirror(tree.root)
	print "After changing the tree to its mirror"
	tree.inorder(tree.root)


