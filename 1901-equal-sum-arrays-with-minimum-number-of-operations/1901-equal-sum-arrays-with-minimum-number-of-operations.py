from typing import List
import heapq

class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        if len(nums1) * 6 < len(nums2) or len(nums2) * 6 < len(nums1):
            return -1  # impossible to match sums

        sum1, sum2 = sum(nums1), sum(nums2)

        if sum1 == sum2:
            return 0

        # Ensure sum1 is smaller
        if sum1 > sum2:
            nums1, nums2 = nums2, nums1
            sum1, sum2 = sum2, sum1

        # Gains for increasing nums1 (values: 6 - num)
        min_heap = [6 - num for num in nums1 if 6 - num > 0]
        # Gains for decreasing nums2 (values: num - 1)
        max_heap = [num - 1 for num in nums2 if num - 1 > 0]

        # Use max-heaps: invert signs
        min_heap = [-x for x in min_heap]
        max_heap = [-x for x in max_heap]
        heapq.heapify(min_heap)
        heapq.heapify(max_heap)

        diff = sum2 - sum1
        ops = 0

        while diff > 0:
            gain1 = -min_heap[0] if min_heap else 0
            gain2 = -max_heap[0] if max_heap else 0

            if gain1 == 0 and gain2 == 0:
                return -1  # No possible gains left

            if gain1 >= gain2:
                diff -= gain1
                heapq.heappop(min_heap)
            else:
                diff -= gain2
                heapq.heappop(max_heap)

            ops += 1

        return ops
