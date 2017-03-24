# -*- coding: UTF-8 -*-

# Iterative preorder traversal

import binary_tree

def iterative_preorder(root):
	if root is None:
		return

	stack = [root]
	curr = root
	done = False

	while stack:
		s = stack[-1]
		print s.data
		del stack[-1]

		if s.right:
			stack.append(s.right)

		if s.left:
			stack.append(s.left)

tree = binary_tree.construct_binary_tree()
iterative_preorder(tree.root)