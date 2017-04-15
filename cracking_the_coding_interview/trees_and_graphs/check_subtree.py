# -*- coding: UTF-8 -*-

'''
	Problem: T1 and T2 are two very large binary trees, with T1 much bigger than T2. Create an algorithm to determine
	if T2 is a subtree of T1.


	Solution: Iterate through the first tree and search for the root node of the second tree. When found, call the helper
	function match_subtree to check if each node in the subtree of the matched nodes matches each other. Wherever it fails,
	return False.

'''

def check_subtree(root1, root2):
	''' Match the root node of T2 with each node of T1 and when matched call match_subtree '''

	if root1 is None:
		return False

	if root1.data == root2.data and matched_subtree(root1, root2):
		return True

	return check_subtree(root1.left, root2) or check_subtree(root1.right, root2)

def matched_subtree(root1, root2):
	''' Check if the two trees are equal by matching each node with each other '''

	if root1 is None and root2 is None:
		return True

	if root1 is None or root2 is None:
		return False

	if root1.data != root2.data:
		return False

	return matched_subtree(root1.left, root2.left) and matched_subtree(root1.right, root2.right)

def main_function():
	''' Initialize the two trees and call check_subtree function '''
	from binary_tree import BinaryTreeNode

	# Initialize the root node of T1
	root1 = BinaryTreeNode(5)

	# Initialize the child nodes
	child_1 = BinaryTreeNode(4)
	child_2 = BinaryTreeNode(6)
	child_child_1 = BinaryTreeNode(3)
	child_child_2 = BinaryTreeNode(1) 
	child_child_3 = BinaryTreeNode(13) 
	child_child_4 = BinaryTreeNode(12) 

	# Connect the child nodes to the parent node
	child_1.add_left(child_child_1)
	child_1.add_right(child_child_2)
	child_2.add_left(child_child_3)
	child_2.add_right(child_child_4)
	root1.add_left(child_1)
	root1.add_right(child_2)


	# Initialize root node of T2
	root2 = BinaryTreeNode(6)

	child1 = BinaryTreeNode(13)
	child2 = BinaryTreeNode(12)
	root2.add_left(child1)
	root2.add_right(child2)

	print check_subtree(root1, root2)

if __name__ == "__main__":
	main_function()
