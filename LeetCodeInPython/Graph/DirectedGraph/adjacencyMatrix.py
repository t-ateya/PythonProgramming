class Graph:
    def __init__(self, number_of_nodes) -> None:
        self.number_of_nodes = number_of_nodes + 1
        self.graph = [[0 for x in range(number_of_nodes + 1)]
                        for y in range(number_of_nodes + 1)]

    def withinBound(self, v1, v2):
        return (v1 >=0 and v1 <= self.number_of_nodes) and (v2 >=0 and v2 <= self.number_of_nodes)

    def insertEdge(self, v1, v2):
        if(self.withinBound(v1, v2)):
            self.graph[v1][v2]  = 1

    def printGraph(self):
        for i in range(self.number_of_nodes):
            for j in range(len(self.graph[i])):
                if (self.graph[i][j]):
                    print(i, "->", j)

g = Graph(5)

g.insertEdge(1, 2)
g.insertEdge(2, 3)
g.insertEdge(4, 5)

g.printGraph()