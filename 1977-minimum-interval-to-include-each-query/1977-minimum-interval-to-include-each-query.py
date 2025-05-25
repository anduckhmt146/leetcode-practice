from typing import List
import heapq

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        sorted_queries = sorted((q, i) for i, q in enumerate(queries))
        
        result = [-1] * len(queries)
        min_heap = []
        i = 0  # Pointer for intervals

        for q, idx in sorted_queries:
            # Add all intervals where start ≤ q
            while i < len(intervals) and intervals[i][0] <= q:
                start, end = intervals[i]
                if end >= q:
                    heapq.heappush(min_heap, (end - start + 1, end))
                i += 1

            # Remove intervals from heap that end < q
            while min_heap and min_heap[0][1] < q:
                heapq.heappop(min_heap)

            if min_heap:
                result[idx] = min_heap[0][0]  # Length of smallest valid interval

        return result
