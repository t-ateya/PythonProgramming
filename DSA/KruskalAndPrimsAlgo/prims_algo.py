
import sys

class Graph:
    def __init__(self, vertex_num, edges, nodes):
        self.edges = edges
        self.nodes = nodes 
        self.number_of_vertices = vertex_num
        self.MST = [] #minimum spanning tree


    def print_solution(self):
        print("Edge : Weight")
        for src, dst, weight in self.MST:
            print("%s -> %s: %s" %(src, dst, weight))

    def prims_algorithm(self):
        visited = [0]*self.number_of_vertices
        edge_num = 0
        visited[0] = True 
        while edge_num < self.number_of_vertices-1:
            min_weight = sys.maxsize #Infinity
            for i in range(self.number_of_vertices):
                if visited[i]:
                    for j in range(self.number_of_vertices):
                        if ((not visited[j]) and self.edges[i][j]):
                            if min_weight > self.edges[i][j]:
                                min_weight = self.edges[i][j]
                                s = i 
                                d = j
            self.MST.append([self.nodes[s], self.nodes[d], self.edges[s][d]])
            visited[d] = True
            edge_num +=1


edges = [
            [0, 10, 20, 0, 0],
            [10, 0, 30, 5, 0],
            [20, 30, 0, 15, 6],
            [0, 5, 15, 0, 8],
            [0, 0, 6, 8, 0]

]

nodes = ["A", "B", "C", "D", "E"]
g = Graph(5, edges, nodes)
g.prims_algorithm()
g.print_solution()