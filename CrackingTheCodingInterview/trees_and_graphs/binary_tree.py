# -*- coding: UTF-8 -*-

class BinaryTreeNode(object):
	''' 
		Class to represent a binary tree node
	'''
	def __init__(self, data):
		self.data = data
		self.children = []

	def add(self, child):
		'''
			Add the child node
		'''
		self.children.append(child)

	def __str__(self):
		text = str(self.data)
		text +=   ': {' + ', '.join([str(child) for child in self.children]) + "} "
		
		return text

def initialize():
	tree = BinaryTreeNode(5)

	# Initialize the child nodes
	child_1 = BinaryTreeNode(4)
	child_2 = BinaryTreeNode(6)
	child_child = BinaryTreeNode(3)

	# Connect the child nodes to the parent node
	child_1.add(child_child)
	tree.add(child_1)
	tree.add(child_2)

	print(tree)