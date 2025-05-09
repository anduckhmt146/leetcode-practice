from typing import List

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Step 1: Initialize distances array with "infinite" cost
        prices = [float('inf')] * n
        prices[src] = 0
        
        # Step 2: Run the Bellman-Ford algorithm for k+1 times
        for i in range(k + 1):
            tmp = prices.copy()
            for u, v, w in flights:
                if prices[u] == float('inf'):
                    continue
                if prices[u] + w < tmp[v]:
                    tmp[v] = prices[u] + w
            prices = tmp
        
        return -1 if prices[dst] == float('inf') else prices[dst]
