class Graph:
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict

    def bfs(self, start_vertex, end_vertex):
        queue = []
        queue.append([start_vertex])
        while queue:
            path = queue.pop(0)
            node = path[-1]
            if node == end_vertex:
                return path 
            for adjacent in self.gdict.get(node, []):
                new_path = list(path)
                new_path.append(adjacent)
                queue.append(new_path)