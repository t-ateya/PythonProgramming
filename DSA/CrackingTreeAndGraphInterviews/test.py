n = 3
#print(int(n/2))
#print((n/2))

#print(1 > 2)
projects = ["a", "b", "c", "d", "e", "f"]
dependencies = [("a","d"), ("f","b"), ("b", "d"), ("f","a"), ("d","c")]
project_graph = {}

for proj in projects:
    project_graph[proj] = []

print(project_graph)


for pairs in dependencies:
    project_graph[pairs[0]].extend(pairs[1])

print(project_graph)