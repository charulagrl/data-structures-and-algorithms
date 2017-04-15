# -*- coding: UTF-8 -*-

import binary_tree

def height(root):
	if not root:
		return 0

	else:
		return max(height(root.left), height(root.right)) + 1

def diameter(root):
	if not root:
		return 0

	else:
		lh = height(root.left)
		rh = height(root.right)

		ld = diameter(root.left)
		rd = diameter(root.right)

		return max(lh+rh+1, max(ld, rd))

tree = binary_tree.construct_binary_tree()
print diameter(tree.root)