# -*- coding: UTF-8 -*-

# Level order traversal

import binary_tree

def level_order_traversal(root):
	if not root:
		return

	queue = [root]

	while queue:
		s = queue[0]
		print s.data
		del queue[0]

		if s.left:
			queue.append(s.left)

		if s.right:
			queue.append(s.right)


tree = binary_tree.construct_binary_tree()
level_order_traversal(tree.root)
	