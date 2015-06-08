# -*- coding: UTF-8 -*-

# Program to find hamiltonian cycle in a graph

import graph 

def isSafe(graph, path, v, i):
	if i in graph.edges[v] and i not in path:
		return True
	return False

def hamiltonian_cycle_util(graph, path, v):
	if v == graph.V-1:
		if 0 in graph.edges[path[-1]]:
			path.append(0)
			print path
			return True
		else:
			return False
	else:
		for i in range(graph.V):
			if isSafe(graph, path, v, i):
				path.append(v)
				if hamiltonian_cycle_util(graph, path, v+1):
					return True
				# Backtrack
				del path[-1]

		return False


graph = graph.construct_graph_undirected()

print hamiltonian_cycle_util(graph, [0], 1)