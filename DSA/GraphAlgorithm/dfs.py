
class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []
            return True 
        return False

    def print_graph(self):
        for vertex in self.adjacency_list:
            print(vertex, ":", self.adjacency_list[vertex])

    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.adjacency_list.keys() and vertex2 in self.adjacency_list.keys():
            self.adjacency_list[vertex1].append(vertex2)
            self.adjacency_list[vertex2].append(vertex1)
            return True 
        return False
    
    def remove_edge(self, vertex1, vertex2):
        if vertex1 in self.adjacency_list.keys() and vertex2 in self.adjacency_list.keys():
            try:
                self.adjacency_list[vertex1].remove(vertex2)
                self.adjacency_list[vertex2].remove(vertex1)
            except ValueError:
                pass
            return True
        return False

    def remove_vertex1(self, vertex):
        """Removes a vertex from the graph.This is my own solution"""
        if vertex in self.adjacency_list.keys():
            [self.remove_edge(vertex, v) for v in self.adjacency_list.keys()]
            self.adjacency_list.pop(vertex)
            return True 
        return False

    def remove_vertex(self, vertex):
        if vertex in self.adjacency_list:
            for other_vertex in self.adjacency_list[vertex]:
                self.adjacency_list[other_vertex].remove(vertex)
            del self.adjacency_list[vertex]
            return True 
        return False

    def bfs(self, vertex):
        """Traverses a graph using breadth first search"""
        visited = [vertex]
        queue = [vertex]
        while queue:
            de_vertex = queue.pop(0)
            print(de_vertex)
            for adjacent_vertex in self.adjacency_list[de_vertex]:
                if adjacent_vertex not in visited:
                    visited.append(adjacent_vertex)
                    queue.append(adjacent_vertex)

    def dfs(self, vertex):
        """Traverses a graph using depth first algo"""
        visited = [vertex]
        stack = [vertex]
        while stack:
            pop_vertex = stack.pop()
            print(pop_vertex)
            for adjacent_vertex in self.adjacency_list[vertex]:
                if adjacent_vertex not in visited:
                    visited.append(adjacent_vertex)
                    stack.append(adjacent_vertex)


        
            

graph = Graph()
graph.add_vertex("A")
graph.add_vertex("B")
graph.add_vertex("C")
graph.add_vertex("D")
graph.add_edge("A", "B")
graph.add_edge("A", "C")
graph.add_edge("B", "C")
#graph.print_graph()

graph.dfs("A")