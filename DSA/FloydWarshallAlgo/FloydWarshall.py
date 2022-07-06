INF = 9999

def print_solution(nV, distance):
    """nV == number of vertices"""
    for i in range(nV):
        for j in range(nV):
            if (distance[i][j] == INF):
                print("INF", end=" ")
            else:
                print(distance[i][j], end = " ")
        print(" ")

def floydWarShall(nV, G):
    distance = G
    for k in range(nV):
        for row in range(nV):
            for col in range(nV):
                distance[row][col] = min(distance[row][col], distance[row][k] + distance[k][col])
    print_solution(nV, distance)


G = [
    [0, 8, INF, 1],
    [INF, 0, 1, INF],
    [4, INF, 0, INF],
    [INF, 2, 9, 1],
]

floydWarShall(4, G)