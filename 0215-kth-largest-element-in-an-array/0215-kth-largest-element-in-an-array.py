import heapq

class Solution:
    # IDEA: Min Heap to pop min
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Use a max-heap (invert distances)
        min_heap = []

        for num in nums:
            heapq.heappush(min_heap, num)

            if len(min_heap) > k:
                heapq.heappop(min_heap)

        return min_heap[0]
        