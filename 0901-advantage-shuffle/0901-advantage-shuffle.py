class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        max_heap = [(-val, idx) for idx, val in enumerate(nums2)]
        heapq.heapify(max_heap)

        result = [0] * len(nums1)
        low = 0
        high = len(nums1) - 1

        while max_heap:
            val, idx = heapq.heappop(max_heap)
            val = -val
            # If the largest in nums1 can beat the largest in nums2
            if nums1[high] > val:
                result[idx] = nums1[high]
                high -= 1
            else:
                # Use the smallest number — sacrifice it
                result[idx] = nums1[low]
                low += 1

        return result