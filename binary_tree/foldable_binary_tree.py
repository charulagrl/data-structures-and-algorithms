# -*- coding: UTF-8 -*-

# Foldable Binary Tree. Program to find if a tree can be folded or not

import binary_tree

def mirror(root1, root2):
	if not root1 and not root2:
		return True
	elif not root1 or not root2:
		return False
	elif mirror(root1.right, root2.left) and mirror(root1.left, root2.right):
			return True
	else:
			return False

def foldable_tree(root):
	if root is None:
		return True

	else:
		if mirror(root.left, root.right):
			return True
		else:
			return False

tree = binary_tree.construct_binary_tree()

print foldable_tree(tree.root)