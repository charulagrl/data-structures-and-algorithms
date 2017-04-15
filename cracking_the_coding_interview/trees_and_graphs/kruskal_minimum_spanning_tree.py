# -*- coding: UTF-8 -*-

'''
	Spanning Tree: Given an undirected and connected graph G=(V, E), a spanning tree of the graph G is a tree that spans G 
	(that is, it includes every vertex of G) and is a subgraph of G (every edge in the tree belongs to G).

	Minimum Spanning Tree: The cost of the spanning tree is the sum of the weights of all the edges in the tree. 
	There can be many spanning trees. Minimum spanning tree is the spanning tree where the cost is minimum among all 
	the spanning trees.
'''

import graph
from union_find_algorithm import get_parent, initialize_parent


def sort_edges(g):
	''' Soft the edges of the graph by weight '''
	num_edges = len(g.edges)

	for i in range(num_edges):
		for j in range(i+1, num_edges):
			if g.edges[i] > g.edges[j]:
				g.edges[i], g.edges[j] = g.edges[j], g.edges[i]

def minimum_spanning_tree(g):
	''' Return the minimum spanning tree of a graph '''
	mst = []
	minimumCost = 0
	parent = initialize_parent(g)

	for edge in g.edges:
		src = edge.src.name
		dest = edge.dest.name

		# If the current edge do not form a cycle
		if (get_parent(src, parent) != get_parent(dest, parent)):
			minimumCost += edge.weight
			parent[src] = dest
			mst.append(edge)
		
	return mst, minimumCost


if __name__ == "__main__":
	g = graph.create_graph()

	sort_edges(g)
	mst, minimumCost = minimum_spanning_tree(g)
	
	for edge in mst:
		print edge

	print "minimum cost is ", minimumCost

