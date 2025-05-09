from typing import List
from collections import defaultdict

class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)

        discovery = [-1] * n
        low = [-1] * n
        time = [0]
        result = []

        def dfs(node, parent):
            discovery[node] = low[node] = time[0]
            time[0] += 1

            for neighbor in graph[node]:
                if neighbor == parent:
                    continue
                if discovery[neighbor] == -1:
                    dfs(neighbor, node)
                    low[node] = min(low[node], low[neighbor])
                    if low[neighbor] > discovery[node]:
                        result.append([node, neighbor])
                else:
                    low[node] = min(low[node], discovery[neighbor])

        dfs(0, -1)
        return result
