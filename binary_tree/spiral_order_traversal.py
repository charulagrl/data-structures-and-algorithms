# -*- coding: UTF-8 -*-

# Print spiral order traversal using iterative method using two stacks

import binary_tree

def spiral_order_traversal(root):
	if not root:
		return

	s1 = [root]
	s2 = []

	while s1 or s2:

		while s1:
			s = s1[0]
			print s.data
			del s1[0]

			if s.right:
				s2.append(s.right)

			if s.left:
				s2.append(s.left)

		while s2:
			s = s2[0]
			print s.data
			del s2[0]

			if s.left:
				s1.append(s.left)

			if s.right:
				s1.append(s.right)

tree = binary_tree.construct_binary_tree()
spiral_order_traversal(tree.root)