class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [-1] * n
        stack = []
        
        for i in range(2 * n - 1, -1, -1):
            curr_idx = i % n
            
            while stack and nums[stack[-1]] <= nums[curr_idx]:
                stack.pop()
                
            if stack:
                result[curr_idx] = nums[stack[-1]]
            
            stack.append(curr_idx)
            
        return result