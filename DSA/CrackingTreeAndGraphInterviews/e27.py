
"""
    Build Order

    You are given a list of projects and a list of dependencies (which is a list of pairs projects, where the second project
    is dependent on the first poject). All of a project's dependencies must be built before the project is. Find a build order
    that will allow the projects to be built. If there is no valid build order, return an error

    Input:
        Projects: a, b, c, d, e, f
        Dependencies: (a,d), (f,b), (b, d), (f,a), (d,c)

    Output:
        e,f,a,b,d,c

    Solution:
    - Use directed graph
    - Find nodes with dependencies
            a, b, c, d
    - Find nodes without dependencies
            e, f

    - Find order by taking out nodes without dependencies
"""

def create_graph(projects, dependencies):
    """Returns a graph based on dependencies and functions"""
    project_graph = {}

    for proj in projects:
        project_graph[proj] = []

    for pairs in dependencies:
        project_graph[pairs[0]].extend(pairs[1])

    return project_graph


def get_project_with_dependencies(graph):
    project_with_dependencies = set()
    for project in graph:
        project_with_dependencies = project_with_dependencies.union(set(graph[project]))
    return project_with_dependencies

def get_projects_without_dependencies(project_with_D, graph):
    project_wo_D = set()
    for proj in graph:
        if not proj in project_with_D:
            project_wo_D.add(proj)
    return project_wo_D

def find_build_order(projects, dependencies):
    build_order = []
    project_graph = create_graph(projects, dependencies)
    while project_graph:
        project_with_dependencies = get_project_with_dependencies(project_graph)
        project_without_dependencies = get_projects_without_dependencies(project_with_dependencies, project_graph)
        if len(project_without_dependencies) ==0 and project_graph:
            raise ValueError("There is a cycle in the build order")
        for independent_projects in project_without_dependencies:
            build_order.append(independent_projects)
            del project_graph[independent_projects]

    return build_order

projects = ["a", "b", "c", "d", "e", "f"]
dependencies = [("a","d"), ("f","b"), ("b", "d"), ("f","a"), ("d","c")]
print(find_build_order(projects, dependencies))
