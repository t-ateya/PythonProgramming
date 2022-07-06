"""
    It is a greedy algorithm
    It finds a minimum spanning tree for weighted undirected graphs in the following ways

    1. Take any vertex as a source, set its weight to 0 and all other vertices' weight to infinity.
    2. For every adjacent vertices, if the current weight is more than current edge, then we set it to current weight.
    3. Then we mark current vertex as visited
    4. Repeat these steps for all vertices in increasing order of weight
"""