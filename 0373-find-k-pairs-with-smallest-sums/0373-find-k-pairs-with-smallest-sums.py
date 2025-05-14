import heapq
from typing import List

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        if not nums1 or not nums2 or k == 0:
            return []

        min_heap = []
        result = []

        # Initialize the heap with the first element in nums2 paired with the first k elements in nums1
        for i in range(min(k, len(nums1))):
            heapq.heappush(min_heap, (nums1[i] + nums2[0], i, 0))

        while min_heap and len(result) < k:
            curr_sum, i, j = heapq.heappop(min_heap)
            result.append([nums1[i], nums2[j]])

            # If there is another element in nums2 for the same nums1[i], push it to the heap
            if j + 1 < len(nums2):
                heapq.heappush(min_heap, (nums1[i] + nums2[j + 1], i, j + 1))

        return result
