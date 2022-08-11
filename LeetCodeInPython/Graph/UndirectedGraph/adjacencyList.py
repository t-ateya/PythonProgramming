

from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def insertEdge(self, v1,v2):
        self.graph[v1].append(v2)
        self.graph[v2].append(v1)

    def printGraph(self):
        for vertex in self.graph:
            for value in self.graph[vertex]:
                print(vertex, "=>", value)

graph = Graph()

graph.insertEdge(1, 5)
graph.insertEdge(1, 100)
graph.insertEdge(5, 2)
graph.insertEdge(2, 7)
graph.insertEdge(7, 1)

graph.printGraph()

