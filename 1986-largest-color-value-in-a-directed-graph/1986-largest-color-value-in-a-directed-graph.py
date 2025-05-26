from collections import defaultdict, deque
from typing import List

class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n = len(colors)
        graph = defaultdict(list)
        in_degree = [0] * n
        
        for u, v in edges:
            graph[u].append(v)
            in_degree[v] += 1
        
        # color_count[i][c] = max count of color c in any path ending at node i
        color_count = [[0] * 26 for _ in range(n)]
        
        queue = deque()
        for i in range(n):
            if in_degree[i] == 0:
                queue.append(i)
                color_count[i][ord(colors[i]) - ord('a')] = 1

        visited = 0
        max_color_value = 0
        
        while queue:
            node = queue.popleft()
            visited += 1
            for neighbor in graph[node]:
                for c in range(26):
        # "For node i, what is the max number of times each color can appear on a path ending at i?"
                    color_count[neighbor][c] = max(
                        color_count[neighbor][c],
                        color_count[node][c] + (1 if c == ord(colors[neighbor]) - ord('a') else 0)
                    )
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
            max_color_value = max(max_color_value, max(color_count[node]))
        
        return max_color_value if visited == n else -1
