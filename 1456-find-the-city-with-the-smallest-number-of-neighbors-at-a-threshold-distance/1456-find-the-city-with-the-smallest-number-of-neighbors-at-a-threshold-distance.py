from typing import List

class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        # Step 1: Initialize distance matrix
        dist = [[float('inf')] * n for _ in range(n)]
        
        for i in range(n):
            dist[i][i] = 0
        
        for u, v, w in edges:
            dist[u][v] = w
            dist[v][u] = w  # Because the graph is undirected
        
        # Step 2: Floyd-Warshall to compute all-pairs shortest paths
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][j] > dist[i][k] + dist[k][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
        
        # Step 3: Count reachable cities within distanceThreshold
        min_reachable = n
        city_index = -1
        
        for i in range(n):
            # Number of nodes can reachable
            count = sum(1 for j in range(n) if i != j and dist[i][j] <= distanceThreshold)
            if count <= min_reachable:
                min_reachable = count
                city_index = i  # Prefer the city with the greatest number in case of tie
        
        return city_index
