# -*- coding: UTF-8 -*-

# Program to initialize a graph and edge

class Edge(object):
	def __init__(self, src=None, dest=None):
		self.src=src
		self.dest=dest

class Graph(object):
	def __init__(self, V=None, edges=[]):
		self.V = V
		self.edges = edges

def construct_graph():
	graph = Graph(4, [None]*4)
	
	graph.edges = [[] for i in graph.edges]

	edge = Edge(0, 1)
	graph.edges[edge.src].append(edge.dest)

	edge = Edge(0, 2)
	graph.edges[edge.src].append(edge.dest)

	edge = Edge(1, 2)
	graph.edges[edge.src].append(edge.dest)

	edge = Edge(2, 0)
	graph.edges[edge.src].append(edge.dest)

	edge = Edge(2, 3)
	graph.edges[edge.src].append(edge.dest)

	edge = Edge(3, 3)
	graph.edges[edge.src].append(edge.dest)

	return graph
