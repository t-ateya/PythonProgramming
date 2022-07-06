

class Graph:
    def __init__(self, g_dict=None):
        if g_dict is None:
            g_dict = {}
        self.graph_dict = g_dict

    def addEdge(self, vertex, edge):
        self.graph_dict[vertex].append(edge)

custom_dic = {
        "a":["b", "c"],
        "b":["a","d", "e"],
        "c": ["a", 'e'],
        "d":["b","e", "f"],
        "e":["b", "c","d"],
        "f":["d", "e"],
}

graph = Graph(custom_dic)
graph.addEdge("e", "f")
print(graph.graph_dict)