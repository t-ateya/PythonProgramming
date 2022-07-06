"""
    Route Between Nodes
    Problem Statement
    Given a directed graph and two nodes(S and E), design an algorithm to find out whether there's a route from S to E

    Solution: Pseudocode
    - Create a function with two parameters, start and end nodes
    - Create queue and enqueue start node to it
    - Find all the neighbors of the just enqueued node and enqueue them into the queue
    - Repeat this process until the end of elements in the graph
    - If during the above process at some point in time we encounter the destination node, we return True
    - Mark visited nodes as visited



"""

class Graph:
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict
    
    def addEdge(self, vertex, edge):
        self.gdict[vertex].append(edge)
    
    def checkRoute(self, startNode, endNode):
        """My Solution"""
        for node in self.gdict[startNode]:
            if endNode in self.gdict[node]:
                return True
        return False  

    def check_route(self, start_node, end_node):
        """Instructor's solution"""
        visited = [start_node]
        queue = [start_node]
        path = False
        while queue:
            de_vertex = queue.pop(0)
            for adjacent_vertex in self.gdict[de_vertex]:
                if adjacent_vertex not in visited:
                    if adjacent_vertex == end_node:
                        path = True
                        break
                    else:
                        visited.append(adjacent_vertex)
                        queue.append(adjacent_vertex)
        return path 

                    


custom_dict = { "a": ["c", "d", "b"],
                "b" : ["j"],
                "c" : ["g"],
                "d" : [],
                "e" : ["f", "a"],
                "f" : ["i"],
                "g" : ["d", "h"],
                "h" : [],
                "i" : [],
                "j" : [],

}

g = Graph(custom_dict)

print(g.checkRoute("e", "i"))
print(g.check_route("e", "i"))