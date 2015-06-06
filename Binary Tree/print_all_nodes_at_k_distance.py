# -*- coding: UTF-8 -*-

# Print all the nodes that are at the kth distance from the root node

import binary_tree

def all_nodes_at_k_distance(node, k):

	if node is None:
		return

	if k == 0:
		print node.data

	all_nodes_at_k_distance(node.left, k-1)
	all_nodes_at_k_distance(node.right, k-1)


if __name__=="__main__":
	tree = binary_tree.construct_binary_tree()

	print "Nodes at kth distance"
	all_nodes_at_k_distance(tree.root, 1)