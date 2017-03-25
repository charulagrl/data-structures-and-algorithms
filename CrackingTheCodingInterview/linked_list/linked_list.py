# -*- coding: UTF-8 -*-

from __future__ import print_function

# Class to represent a single node in a linked list
class Node(object):

	def __init__(self, data, nextnode=None):
		self.data = data
		self.nextnode = nextnode

# Class to represent a linked list
class LinkedList(object):

	def __init__(self, head=None):
		self.head = head


	# Function to insert an element in a linked list
	def insert(self, data):

		node = Node(data, None)

		if self.head == None:
			self.head = node

		else:

			node.nextnode = self.head
			self.head = node

	# Function to delete a node at a particular position in linked list
	def delete_at_position(self, position):

		if head == None:
			raise ValueError("Linked list is empty")

		index = 0
		current = self.head

		while (index < position-1 and current.nextnode):
			current = current.nextnode
			index += 1

		if not current.nextnode:
			# TODO: Do proper exception handline in Python
			return "Linked list index out of range"

		current.nextnode = current.nextnode.nextnode

	# Function to get the size of the linked list
	def get_size(self):

		count = 0
		current = self.head
		while current:
			count += 1
			current = current.nextnode

	# Function to check if the linked list is empty
	def is_empty(self):

		if not self.head:
			return True

		return False

	# Function to print the elements in a linked list
	def print(self):

		if not self.head:
			raise ValueError("List is empty")

		current = self.head
		while current:
			print(current.data, end=" ")
			current = current.nextnode
