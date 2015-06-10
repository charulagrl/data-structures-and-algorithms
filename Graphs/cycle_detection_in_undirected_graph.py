# -*- coding: UTF-8 -*-

# Program to detect cycle in an undirected graph

import graph 

def detect_cycle_util(graph, start, visited, parent):

	visited.append(start)

	for edge in graph.edges[start]:
		if edge not in visited:
			if detect_cycle_util(graph, edge, visited, start):
				return True

		elif edge != parent:
			return True

	return False

def detect_cycle(graph):

	visited = []

	for i in range(graph.V):
		if i not in visited:
			if detect_cycle_util(graph, i, visited, -1):
				return True

	return False

graph = graph.construct_graph_undirected()

print detect_cycle(graph)