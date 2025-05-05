import heapq
from collections import defaultdict

class Solution:

    def networkDelayTime(self, times, n, k):
        # Build adjacency list
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        # Dijkstra Min-heap to track the shortest path: (current_cost, current_node)
        heap = [(0, k)]
        visited = {}

        while heap:
            time, node = heapq.heappop(heap)

            # Skip if already visited
            if node in visited:
                continue

            visited[node] = time

            for neighbor, weight in graph[node]:
                if neighbor not in visited:
                    heapq.heappush(heap, (time + weight, neighbor))

        # k = 2, value: {2: 0, 1: 1, 3: 1, 4: 2}
        print(visited)

        # If all nodes are visited, return the max time; else, -1
        return max(visited.values()) if len(visited) == n else -1
