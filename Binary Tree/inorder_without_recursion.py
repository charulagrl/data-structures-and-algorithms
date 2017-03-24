# -*- coding: UTF-8 -*-

import binary_tree

# Program to print inorder traversal of tree without using recursion

def inorder_without_recursion(node):
	if node is None:
		return

	stack = []
	curr = node
	done = False

	while(not done):

		if curr:
			stack.append(curr)
			curr = curr.left

		else:
			if stack:
				temp = stack[-1]
				print temp.data
				del stack[-1]

				if temp.right != None:
					curr = temp.right

			else:
				done = True

if __name__=='__main__':
	tree = binary_tree.construct_binary_tree()

	print "without recursion"
	inorder_without_recursion(tree.root)