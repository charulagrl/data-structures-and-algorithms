# -*- coding: UTF-8 -*-

# Program to print the maximum width of a tree

import binary_tree

def max_width(tree):

	h = tree.height(tree.root)

	# count stores the number of nodes at each level
	count = [0] * h

	level = 0

	count = max_width_util(tree.root, count, level)

	return max(count)

def max_width_util(root, count, level):

	if root:
		count[level] += 1
		max_width_util(root.left, count, level+1)
		max_width_util(root.right, count, level+1)

	return count

def max(count):

	maximum = count[0]

	for i in range(1, len(count)):
		if count[i] > maximum:
			maximum = count[i]

	return maximum

if __name__=="__main__":
	tree = binary_tree.construct_binary_tree()
	print "Printing max width of tree"
	print max_width(tree)