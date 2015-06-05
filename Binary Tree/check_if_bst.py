# Program to check if the binary tree is a binary search tree(BST) or not

import binary_tree

def check_if_bst(node):

	if node == None:
		return True

	# false if left is greater than node
	if node.left and node.left.data > node.data:
		return False

	# false if right is less than node
	if node.right and node.right.data < node.data:
		return False

	# false if any of the sub tree is not bst
	if not check_if_bst(node.left) or not check_if_bst(node.right):
		return False

	# else true
	return True

if __name__=="__main__":
	tree = binary_tree.construct_binary_tree()

	print check_if_bst(tree.root)