# -*- coding: UTF-8 -*-

# Program to do a depth first traversal of a graph

import graph

def dfs(graph, start, visited):
	
	print start
	visited.append(start)

	edges = graph.edges[start]
		
	for edge in edges:
		if edge not in visited:	
			dfs(graph, edge, visited)
		

if __name__=='__main__':
	graph = graph.construct_graph()
	dfs(graph, 2, [])
