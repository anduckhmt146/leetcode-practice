class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix = [0] * len(nums)
        for i in range(0, len(nums)):
            prefix[i] = nums[0] if i == 0 else prefix[i - 1] + nums[i]

        postfix = [0] * len(nums)
        
        for i in range(len(nums) - 1, -1, -1):
            postfix[i] = nums[len(nums) - 1] if i == len(nums) - 1 else postfix[i + 1] + nums[i]

        for i in range(len(nums)):
            if prefix[i] == postfix[i]:
                return i

        return -1

        