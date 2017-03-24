# -*- coding: UTF-8 -*-

# PRogram to convert a tree such that it follows child sum property

import binary_tree

def increment(node, diff):
	if node.left != None:
		node.left.data += diff
		increment(node.left, diff)

	elif node.right != None:
		node.right.data += diff
		increment(node.right, diff)

def convert_tree_to_children_sum_property_tree(node):
	if node == None or (node.left == None and node.right == None):
		return

	else:
		convert_tree_to_children_sum_property_tree(node.left)
		convert_tree_to_children_sum_property_tree(node.right)

		left_child_data = 0
		right_child_data = 0

		if node.left:
			left_child_data = node.left.data

		if node.right:
			right_child_data = node.right.data

		diff = node.data - left_child_data - right_child_data
		# print diff
		if diff < 0:
			node.data += abs(diff)

		elif diff > 0:
			increment(node, diff)


if __name__=='__main__':
	root = binary_tree.Node(50)
	
	tree = binary_tree.Tree(root)
	
	root = tree.root
	root.left = binary_tree.Node(7)
	root.right = binary_tree.Node(2)
	root.left.left = binary_tree.Node(3)
	root.left.right = binary_tree.Node(5)
	root.right.left = binary_tree.Node(1)
	root.right.right = binary_tree.Node(30)

	tree.inorder(root)

	convert_tree_to_children_sum_property_tree(root)
	print "After Conversion"
	tree.inorder(root)