import heapq
from typing import List

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        # Min-heap: each entry is (value, row, col)
        heap = []
        
        # Initialize the heap with the first element of each row
        for r in range(min(k, n)):  # We don't need more than k rows
            heapq.heappush(heap, (matrix[r][0], r, 0))
        
        # Extract the smallest element k times
        count = 0
        while heap:
            val, r, c = heapq.heappop(heap)
            count += 1
            if count == k:
                return val
            if c + 1 < n:
                heapq.heappush(heap, (matrix[r][c + 1], r, c + 1))
