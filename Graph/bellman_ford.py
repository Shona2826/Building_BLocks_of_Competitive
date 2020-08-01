import sys
from collections import defaultdict

class Graph:

	def __init__(self,vertices):
		self.V = vertices
		self.graph = []

	def addEdge(self,u,v,w):
		self.graph.append([u,v,w])

	def printArr(self,dist):
		for i in range(self.V):
			print(i,"   ",dist[i])
	def bellman_ford(self,src):
		dist = [sys.maxsize]*self.V
		dist[src] = 0
		for _ in range(self.V - 1):
			for u,v,w in self.graph:
				
				if dist[u] != float("Inf") and dist[u] + w < dist[v]:
					dist[v] = dist[u]+w

		for u,v,w in self.graph:
			if dist[u] != float("Inf") and dist[u] + w < dist[v]:
				print("Contains negative weight cycle")
				return 

		self.printArr(dist)

g = Graph(5)  
g.addEdge(0, 1, -1)  
g.addEdge(0, 2, 4)  
g.addEdge(1, 2, 3)  
g.addEdge(1, 3, 2)  
g.addEdge(1, 4, 2)  
g.addEdge(3, 2, 5)  
g.addEdge(3, 1, 1)  
g.addEdge(4, 3, -3)  
  
# Print the solution  
g.bellman_ford(0)