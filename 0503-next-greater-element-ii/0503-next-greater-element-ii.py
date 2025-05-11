from typing import List

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        nums2 = nums + nums  # simulate circular array
        n = len(nums)
        result = [0] * (2 * n)
        stack = []

        # Compute next greater for doubled array
        for i in range(2 * n - 1, -1, -1):
            while stack and stack[-1] <= nums2[i]:
                stack.pop()
            
            if stack:
                result[i] = stack[-1]
            else:
                result[i] = -1

            stack.append(nums2[i])

        print(result)  # optional debug output

        # Instead of using a hashmap (which fails on duplicates), collect result by index
        return result[:n]
