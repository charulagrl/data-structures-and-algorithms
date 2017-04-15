# -*- coding: UTF-8 -*-

# Program for topological sorting of a graph
# takes O(V+E)

class Edge(object):
	def __init__(self, src=None, dest=None):
		self.src=src
		self.dest=dest

class Graph(object):
	def __init__(self, V=None, edges=[]):
		self.V = V
		self.edges = edges

def topological_sort_util(graph, start, visited, stack):
	
	visited[start] = True
	connected_nodes = graph.edges[start]
	
	for node in connected_nodes:
		if not visited[node]:
			topological_sort_util(graph, node, visited, stack)

	stack.append(start)

def topological_sort(graph):

	visited = [False]*graph.V

	stack = []

	for v in range(graph.V):
		if not visited[v]:
			topological_sort_util(graph, v, visited, stack)

	while (stack):
		print stack[-1]
		del stack[-1]
 

if __name__=='__main__':

	graph = Graph(6, [None]*6)
	
	graph.edges = [[] for i in graph.edges]

	edge = Edge(5, 2)
	graph.edges[edge.src].append(edge.dest)

	edge = Edge(5, 0)
	graph.edges[edge.src].append(edge.dest)

	edge = Edge(3, 1)
	graph.edges[edge.src].append(edge.dest)

	edge = Edge(4, 1)
	graph.edges[edge.src].append(edge.dest)

	edge = Edge(2, 3)
	graph.edges[edge.src].append(edge.dest)

	edge = Edge(4, 0)
	graph.edges[edge.src].append(edge.dest)

	print graph.edges

	topological_sort(graph)