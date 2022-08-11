"""
    network delay time: Medium #743
    There are N network nodes, labelled 1 to N. Given times, a list of travel times as directed edges times[i] = (u, v, w)
    where u is the source code, v is the target node, and w is the time it takes for a signal to travel from source to target.
    We will send a signal from a certain node K. How long will it take for all nodes to receive the signal? 
    If it is impossible return -1

    Input: times = [
        [2,1,1],
        [2,3,1],
        [3,4,1]
    ]

    N = 4, k =2

    Solution:
      We implement this usingn Dijkstra's algo
"""
from collections import defaultdict
import heapq

class Solution:
    def networkDelayTime(self, times: list[list[int]], N: int, K:int)->int:
        graph = defaultdict(list)

        for u, v, cost in times:
            graph[u].append((cost, v))

        min_heap = [(0, K)]

        visited = set()
        distance = {i:float('inf') for i in range(1, N+1)}

        distance[K] = 0

        while min_heap:
            cur_distance, u = heapq.heappop(min_heap)
            if u in visited:
                continue
            visited.add(u)

            if len(visited) == N:
                return cur_distance

            for direct_distance, v in graph[u]:
                if cur_distance + direct_distance < distance[v] and v not in visited:
                    distance[v] = cur_distance + direct_distance
                    heapq.heappush(min_heap, (distance[v], v))

        return -1


 


        