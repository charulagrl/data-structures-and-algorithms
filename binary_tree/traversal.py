# -*- coding: UTF-8 -*-

# Program to print level order traversal and spiral order traversal

import binary_tree

def level_order_traversal(root, level):
	
	if not root:
		return

	if level == 1:
		print root.data
	
	elif level > 1:
		level_order_traversal(root.left, level-1)
		level_order_traversal(root.right, level-1)

def spiral_level_order_traversal(root, level, flag):

	if not root:
		return

	if level == 1:
		print root.data

	elif level > 1:

		if flag:
			spiral_level_order_traversal(root.left, level-1, flag)
			spiral_level_order_traversal(root.right, level-1, flag)

		else:
			spiral_level_order_traversal(root.right, level-1, flag)
			spiral_level_order_traversal(root.left, level-1, flag)
			
tree = binary_tree.construct_binary_tree()

height = tree.height(tree.root)
print "Level order traversal"
for i in range(1, height+1):
	level_order_traversal(tree.root, i)

flag = True
print "Spiral level order traversal"
for i in range(1, height+1):
	flag = not flag
	spiral_level_order_traversal(tree.root, i, flag)