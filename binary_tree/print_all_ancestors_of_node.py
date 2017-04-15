# -*- coding: UTF-8 -*-

# Program to find all ancestors of a node in a binary tree

import binary_tree

def find_ancestors(root, node, index, path):

	if root is None:
		return

	if root.data == node:
		print path[0:index]
		return

	else:
		if index < len(path):
			path[index] = root.data
		else:
			path.append(root.data)

		find_ancestors(root.left, node, index+1, path)
		find_ancestors(root.right, node, index+1, path)


tree = binary_tree.construct_binary_tree()
find_ancestors(tree.root, 8, 0, [])

