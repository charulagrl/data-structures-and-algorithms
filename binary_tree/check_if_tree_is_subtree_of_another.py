# -*- coding: UTF-8 -*-

import binary_tree

# Program to check if a tree is subtree of another tree

def check_for_rest_of_tree(tree_a, tree_b):
	if not tree_a and not tree_b:
		return True
	
	elif not tree_b:
		return True
	
	else:
		if tree_a.data == tree_b.data and check_for_rest_of_tree(tree_a.left, tree_b.left) and check_for_rest_of_tree(tree_a.right, tree_b.right):
			return True
		
		else:
			return False

def check_subtree(root, root1):

	if root is None:
		return False

	if root1 is None:
		return True

	else:

		if root.data == root1.data:
			if check_for_rest_of_tree(root, root1):
				return True

		return check_subtree(root.left, root1)
		return check_subtree(root.right, root1)


if __name__=='__main__':

	tree = binary_tree.construct_binary_tree()

	# initialize root node of a tree
	root = binary_tree.Node(10)

	# initialize a binary subtree
	tree1 = binary_tree.Tree(root)

	root.left = binary_tree.Node(4)
	root.right = binary_tree.Node(6)
	root.left.right = binary_tree.Node(3)

	print "tree 1"
	tree.inorder(tree.root)
	print "tree 2"
	tree1.inorder(tree1.root)
	
	print check_subtree(tree.root, tree1.root)

