from typing import List
from collections import Counter
import heapq

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        count = Counter(arr)
        max_heap = [-freq for freq in count.values()]  # Use max-heap
        heapq.heapify(max_heap)
        
        removed = 0
        total_removed = 0
        half = len(arr) // 2

        while total_removed < half:
            freq = -heapq.heappop(max_heap)
            total_removed += freq
            removed += 1

        return removed
