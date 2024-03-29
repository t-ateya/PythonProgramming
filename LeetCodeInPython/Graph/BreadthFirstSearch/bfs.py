

from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def insertEdge(self, u, v):
        self.graph[u].append(v)

    def bsf(self, start_node):
        visited = set()
        queue = []
        queue.append(start_node)

        visited.add(start_node)

        while(queue):
            u = queue.pop(0)
            print(u, end=" ")

            for v in self.graph[u]:
                if v not in visited:
                    queue.append(v)
                    visited.add(v)

g = Graph()

g.insertEdge(2,1)
g.insertEdge(2,5)
g.insertEdge(5,6)
g.insertEdge(5,8)
g.insertEdge(6,9)

g.bsf(2)