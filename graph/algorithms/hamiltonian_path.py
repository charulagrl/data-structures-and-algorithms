# -*- coding: UTF-8 -*-

'''
	Hamiltonian Path

	Hamiltonian Path is a path in a directed or undirected graph that visits each vertex exactly once. The problem to check 
	whether a graph (directed or undirected) contains a Hamiltonian Path is NP-complete, so is the problem of finding all the 
	Hamiltonian Paths in a graph.
'''
from __future__ import print_function
from data_structures.adjacency_list_graph import construct_graph

class HamiltonianPath(object):
	def __init__(self, graph):
		self.graph = graph
		self.vertices = self.graph.adjacency_dict.keys()

	def is_hamitonian(self):
		'''Check if the path exists between the current sequence of vertices'''
		N = len(self.vertices)

		for i in range(N-1):
			if self.vertices[i+1] not in self.graph.get_connected_vertices(self.vertices[i]):
				return False

		return True

	def get_permutations(self, left, right):
		'''Find all the permutation of vertices and return hamiltonian path if it exists'''
		if (left == right):
			if self.is_hamitonian():
				for vertex in self.vertices:
					print (vertex, end=" ")
				print ("\n")
		else:
			for i in range(left, right+1):
				self.vertices[left], self.vertices[i] = self.vertices[i], self.vertices[left]
				self.get_permutations(left+1, right)
				# backtrack
				self.vertices[left], self.vertices[i] = self.vertices[i], self.vertices[left]

	def hamiltonian(self):
		self.get_permutations(0, len(self.vertices)-1)

if __name__ == "__main__":

	g = construct_graph()
	hamiltonian = HamiltonianPath(g)
	hamiltonian.hamiltonian()
