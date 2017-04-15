# -*- coding: UTF-8 -*-

''' 
	Problem: Detect cycle in an undirected graph
'''

import graph

def get_parent(x, parent):
	''' Rreturn the parent of a node until it is 1 '''
	if (parent[x] == -1):
		return x

	return get_parent(parent[x], parent)

def detect_cycle(edges, parent):
	''' Detects if there is a cycle in a graph '''
	for edge in edges:
		src = edge.src.name
		dest = edge.dest.name
		
		if (get_parent(src, parent) == get_parent(dest, parent)):
				return True
		else:
			parent[src] = dest

		print parent
	return False

def initialize_parent(g):
	''' Initialize a parent dict where each node stores its parent node.
		Initially each node is a different subsets with no parent node, hence initialized with -1 '''
	parent = {}
	for vertex in g.vertices:
		parent[vertex.name] = -1

	return parent

if __name__ == "__main__":
	g = graph.create_graph()

	parent = initialize_parent(g)
	print detect_cycle(g.edges, parent)
