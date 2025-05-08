from typing import List
from collections import deque

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        color = [-1] * n  # -1 means unvisited; 0 and 1 are two colors

        for start in range(n):
            if color[start] == -1:
                queue = deque([start])
                color[start] = 0

                while queue:
                    node = queue.popleft()
                    for neighbor in graph[node]:
                        if color[neighbor] == -1:
                            color[neighbor] = 1 - color[node]  # alternate color
                            queue.append(neighbor)
                        elif color[neighbor] == color[node]:
                            return False  # same color on both sides means not bipartite
        return True
