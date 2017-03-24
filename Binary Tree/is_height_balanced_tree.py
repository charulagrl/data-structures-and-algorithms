# -*- coding: UTF-8 -*-

# Programt o check if a tree is height balanced or not. A tree is height balanced if difference in height of left and right subtree is not greater than 1

import binary_tree

def height(root):
		if root is None:
			return 0

		else:
			l = height(root.left)
			r = height(root.right)

			if l > r:
				return l + 1
			else:
				return r + 1

def is_balanced_tree(node):

	if node == None:
		return True

	else:
		l = height(node.left)
		r = height(node.right)

		if abs(l-r) <= 1 and is_balanced_tree(node.left) and is_balanced_tree(node.right):
			return True
		return False

if __name__=="__main__":
	tree = binary_tree.construct_binary_tree()
	print is_balanced_tree(tree.root)