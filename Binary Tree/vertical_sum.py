# -*- coding: UTF-8 -*-

import binary_tree

# Program to find vertical sum of a tree. 
# HD for root is 0, a right edge (edge connecting to right subtree) is considered as +1 horizontal distance and a left edge is considered as -1 horizontal distance. 

def vertical_sum(root, hd, sum_dict):

	if root is None:
		return

	else:
		if hd in sum_dict.keys():
			sum_dict[hd] += root.data
		else:
			sum_dict[hd] = root.data


	vertical_sum(root.left, hd-1, sum_dict)
	vertical_sum(root.right, hd+1, sum_dict)


tree = binary_tree.construct_binary_tree()

sum_dict = {}
vertical_sum(tree.root, 0, sum_dict)

print sum_dict