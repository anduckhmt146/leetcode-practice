# If there are no houses, return 0.
# If there's only one house, return the money in that house.
# For each house, there are two choices:
# You can rob the current house, which means you should add the money from that house to the total amount up to house i-2.
# Or, you can skip robbing the current house, and the total amount will just be the same as the amount up to house i-1.
# Formula:
# dp[i] = max(dp[i-1], nums[i] + dp[i-2])
class Solution:
    def rob(self, nums):
        if not nums:
            return 0
        elif len(nums) == 1:
            return nums[0]
        
        # Initialize the dp array
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], nums[i] + dp[i-2])
        
        return dp[-1]

        

            