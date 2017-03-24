# -*- coding: UTF-8 -*-

# Iterative postorder traversal

import binary_tree

def postorder(root):
	if root is None:
		return

	stack1 = [root]
	stack2 = []

	while stack1:
		s = stack1[-1]
		stack2.append(s)
		del stack1[-1]

		if s.left:
			stack1.append(s.left)

		if s.right:
			stack1.append(s.right)

	while(stack2):

		s = stack2[-1]
		print s.data
		del stack2[-1]


tree = binary_tree.construct_binary_tree()
postorder(tree.root)