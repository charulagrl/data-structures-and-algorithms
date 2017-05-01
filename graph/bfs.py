# -*- coding: UTF-8 -*-

# Program to do a breadth first traversal of a graph

from data_structures import graph

def bfs(graph, start):

	visited = []

	queue = [start]
	visited.append(start)

	while queue:
		# pop the first element of the queue
		s = queue[0]
		print s
		del queue[0]

		for k in graph.edges[s]:
			if k not in visited:
				visited.append(k)
				queue.append(k)

if __name__ == '__main__':
	graph = graph.construct_graph()
	bfs(graph, 2)
