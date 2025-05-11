class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums2)
        result = [0] * n
        stack = []

        for i in range(n - 1, -1, -1):
            while stack and stack[-1] <= nums2[i]:
                stack.pop()
            
            if stack:
                result[i] = stack[-1]
            else:
                result[i] = -1

            stack.append(nums2[i])

        hashMapGreater = {}

        for i in range(len(nums2)):
            hashMapGreater[nums2[i]] = result[i]

        return [hashMapGreater[num] for num in nums1]
        