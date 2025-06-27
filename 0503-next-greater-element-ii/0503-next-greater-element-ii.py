class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        nums2 = nums + nums
        n = len(nums2)

        # Init a stack
        stack = []
        
        # Result array
        res = [0] * n

        # Loop from the end of the array
        # Use stack for reserved order
        for i in range(n - 1, -1, -1):
            #  Remove all smaller elements in stack
            while stack and stack[-1] <= nums2[i]:
                stack.pop()
            
            # Update value
            if stack:
                res[i] = stack[-1]
            else:
                res[i] = -1

            stack.append(nums2[i])

        return res[:len(nums)]
