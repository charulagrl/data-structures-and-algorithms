# -*- coding: UTF-8 -*-

class Edge:
	'''
		Class to represent an edge in a graph
	'''
	def __init__(self, src, dest, weight=None):
		self.src = src
		self.dest = dest
		self.weight = weight

	def __hash__(self):
		return hash((self.src, self.dest))

	def __eq__(self, other):
		return (self.src, self.dest) == (other.src, other.dest)


class Vertex:
	'''
		Class to represent a vertex in a graph
	'''
	def __init__(self, name):
		self.name = name

	def __hash__(self):
		return hash(self.name)

	def __eq__(self, other):
		return self.name == other.name


class AbstractGraph:
	'''
		Abstract class for a graph
	'''
	def add_edge(self, src, dest, weight=None, directed=True):
		raise NotImplementedError
	
	def create_vertex(self, name):
		raise NotImplementedError

	def get_weight(self, src, dest):
		raise NotImplementedError

	def get_edges(self, src):
		raise NotImplementedError


class AdjacencyListGraph(AbstractGraph):
	'''
		Class to represent a graph using adjacency list
	'''
	def __init__(self):
		self.adjacency_dict = {}

	def create_vertex(self, name):
		vertex = Vertex(name=name)

		if vertex not in self.adjacency_dict:
			self.adjacency_dict[vertex] = list()

		return vertex

	def add_edge(self, src, dest, weight=None, directed=True):
		if directed:
			self.add_directed_edge(src, dest, weight)
		else:
			self.add_undirected_edge(src, dest, weight)

	def add_directed_edge(self, src, dest, weight=None):
		edge = Edge(src=src, dest=dest, weight=weight)

		self.adjacency_dict[src].append(edge)

	def add_undirected_edge(self, src, dest, weight=None):
		self.add_directed_edge(src, dest, weight)
		self.add_directed_edge(dest, src, weight)

	def get_weight(self, src, dest):

		adjacency_list = self.adjacency_dict[src]

		for edge in adjacency_list:
			if edge.dest == dest:
				return edge.weight

	def get_edges(self, src):

		return self.adjacency_dict[src]

	def __str__(self):
		
		text = ''

		for vertex, edges in self.adjacency_dict.iteritems():
			text += "{" + str(vertex.name) + ": " + ', '.join([edge.dest.name for edge in edges]) + "}\n"

		return text


def initialize():
	'''
		Function to initialize a graph 
	'''
	# Initialize a graph
	graph = AdjacencyListGraph()

	# Initialize the vertex in the graph
	a = graph.create_vertex("a")
	b = graph.create_vertex("b")
	c = graph.create_vertex("c")
	d = graph.create_vertex("d")
	# Initialize the edges in the graph
	graph.add_edge(a, b, directed=False)
	graph.add_edge(b, c, directed=False)
	graph.add_edge(c, d, directed=False)
	graph.add_edge(d, b, directed=False)
	
	print (graph)




