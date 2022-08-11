"""
    DFS is a recursive algorithm
     -DFS always moves forward till there are no other nodes in current path, else backtrack.
"""
from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def insertEdge(self, v1, v2):
        self.graph[v1].append(v2)

    def DFS(self, startNode):
        visited = set()
        stack = []
        stack.append(startNode)

        while(len(stack)):
            curr = stack[-1]
            stack.pop()

            if (curr not in visited):
                print(curr, end=" ")
                visited.add(curr)

            for vertex in self.graph[curr]:
                if (vertex not in visited):
                    stack.append(vertex)

g = Graph()

g.insertEdge(2,1)
g.insertEdge(2,5)
g.insertEdge(5,6)
g.insertEdge(5,8)
g.insertEdge(6,9)

g.DFS(2)
                    

