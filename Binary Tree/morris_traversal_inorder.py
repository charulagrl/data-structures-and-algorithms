# -*- coding: UTF-8 -*-

# Morris Traversal: Inorder traversal without recursion and stack

import binary_tree

def traverse(root):
	if root is None:
		return 

	curr = root

	while curr:
		if not curr.left:
			print curr.data
			curr = curr.right

		else:
			pre = curr.left

			while pre.right and pre.right != curr:
				pre = pre.right

			if pre.right == None:
				pre.right = curr
				curr = curr.left

			else:
				pre.right = None
				print curr.data
				curr = curr.right

tree = binary_tree.construct_binary_tree()

traverse(tree.root)
