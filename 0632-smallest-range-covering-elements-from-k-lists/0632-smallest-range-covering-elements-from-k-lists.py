from heapq import heappush, heappop
from typing import List

class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        min_heap = []
        max_val = float('-inf')
        
        # Initialize heap with the first element from each list
        for i in range(len(nums)):
            val = nums[i][0]
            heappush(min_heap, (val, i, 0))  # (value, list index, element index)
            max_val = max(max_val, val)
        
        range_start, range_end = float('-inf'), float('inf')

        while True:
            min_val, list_idx, elem_idx = heappop(min_heap)

            # Update the range if smaller
            if max_val - min_val < range_end - range_start:
                range_start, range_end = min_val, max_val
            
            # Move to the next element in the same list
            if elem_idx + 1 == len(nums[list_idx]):
                break  # We've reached the end of one of the lists
            next_val = nums[list_idx][elem_idx + 1]
            heappush(min_heap, (next_val, list_idx, elem_idx + 1))
            max_val = max(max_val, next_val)
        
        return [range_start, range_end]
