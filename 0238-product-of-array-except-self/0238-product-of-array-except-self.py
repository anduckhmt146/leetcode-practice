class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        postfix = [1] * len(nums)
        # Create prefix and postfix list
        for i in range(0, len(nums)):
            prefix[i] = nums[i] if i == 0 else prefix[i - 1] * nums[i]
            postfix[len(nums) - 1 - i] = nums[len(nums) - 1] if i == 0 else postfix[len(nums) - i] * nums[len(nums) - 1 - i]

        # print(prefix)
        # print(postfix)
        
        # Compute result using prefix and postfix
        result = [1] * len(nums)
        for i in range(0, len(nums)):
            left = prefix[i - 1] if i > 0 else 1
            right = postfix[i + 1] if i < len(nums) - 1 else 1
            result[i] = left * right
        
        return result

        