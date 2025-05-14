from typing import List
import heapq

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        sorted_queries = sorted((q, i) for i, q in enumerate(queries))
        result = [-1] * len(queries)
        min_heap = []
        i = 0  # Pointer for intervals

        for query, idx in sorted_queries:
            # Add all intervals starting before or at the query
            while i < len(intervals) and intervals[i][0] <= query:
                start, end = intervals[i]
                if end >= query:
                    heapq.heappush(min_heap, (end - start + 1, end))
                i += 1
            
            # Remove intervals from heap that don't cover the query
            while min_heap and min_heap[0][1] < query:
                heapq.heappop(min_heap)

            if min_heap:
                result[idx] = min_heap[0][0]

        return result
