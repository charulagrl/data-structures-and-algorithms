# -*- coding: UTF-8 -*-

# Program to check if a tree is complete or not

import binary_tree

def check_tree(root):

	if not root:
		return

	queue = [root]
	flag = False

	while queue:

		s = queue[0]
		del queue[0]

		if s.left:
			if flag:
				return False

			queue.append(s.left)

		else:
			flag = True

		if s.right:
			if flag:
				return False

			queue.append(s.right)
		
		else:
			flag = False

	return True

tree = binary_tree.construct_binary_tree()
print check_tree(tree.root)