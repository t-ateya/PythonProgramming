dist = float("Inf")
#d2 = int("Inf")
#d3 = double("Inf")
#print(dist)
#print(d2)

graph = []
graph.append(["A", "C", 6])
graph.append(["A", "B", 12])
graph.append(["B", "C", 6])
graph.append(["D", "E", 11])
print(graph)

[print(x, y, z) for x,y,z in graph]