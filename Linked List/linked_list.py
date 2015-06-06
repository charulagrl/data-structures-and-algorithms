from __future__ import print_function

# Class to initialize a node for a linked list
class Node(object):
	def __init__(self, data):
		self.data = data
		self.nextnode = None


class LinkedList(object):
	def __init__(self, head=None):
		self.head = head

	def search(self, head, data, index):
		if head.data == data:
			print (index)
		else:
			if head.nextnode:
				return self.search(head.nextnode, data, index+1)
			else:
				raise ValueError("Node not in linked list")

	def print_list(self):
		if self.head == None:
			raise ValueError("List is empty")

		current = self.head 
		while(current):
			print (current.data, end="  ")
			current = current.nextnode
		print ('\n')

	def size(self):
		if self.head == None:
			return 0

		size = 0
		current = self.head
		while(current):
			size += 1
			current = current.nextnode

		return size

	def insert(self, data):
		node = Node(data)
		if not self.head:
			self.head = node
		else:
			node.nextnode = self.head
			self.head = node

	def delete(self, data):
		if not self.head:
			return
		
		temp = self.head
		
		if temp.data == data:
			head = temp.nextnode
			print ("Deleted node is " + str(head.data))
			return

		while(temp.nextnode):
			if (temp.nextnode.data == data):
				print ("Node deleted is " + str(temp.nextnode.data))
				temp.nextnode = temp.nextnode.nextnode
				return
			temp = temp.nextnode
		print ("Node not found")
		return