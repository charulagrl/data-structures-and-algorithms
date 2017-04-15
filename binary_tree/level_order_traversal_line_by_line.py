# -*- coding: UTF-8 -*-

# Print level order traversal line by line using iterative level order traversal
# using queue

import binary_tree

def level_order(root):

	queue = []
	queue.append(root)
	
	while 1:

		# keep track of the number of nodes at each level
		nodecounts = len(queue)

		if nodecounts == 0:
			break

		while nodecounts > 0:
			s = queue[0]
			print s.data
			del queue[0]

			if s.left:
				queue.append(s.left)
			if s.right:
				queue.append(s.right)

			nodecounts -= 1

		print "Next level"

tree = binary_tree.construct_binary_tree()

level_order(tree.root)