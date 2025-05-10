from collections import defaultdict, deque
from typing import List

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        # Build the graph with direction info
        graph = defaultdict(list)
        for u, v in connections:
            graph[u].append((v, 1))  # original direction
            graph[v].append((u, 0))  # reverse direction

        visited = set()
        queue = deque([0])
        visited.add(0)
        changes = 0

        while queue:
            current = queue.popleft()
            for neighbor, direction in graph[current]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
                    changes += direction  # increment if we need to reverse this edge

        return changes
