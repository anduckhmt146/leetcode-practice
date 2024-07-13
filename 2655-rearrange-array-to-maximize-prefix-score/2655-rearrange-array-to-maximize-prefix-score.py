class Solution:
    def maxScore(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums, reverse=True)
        N = len(nums)
        prefix = [0] * N
        prefix[0] = sorted_nums[0]
        count = 1 if prefix[0] > 0 else 0
        for i in range(1, N):
            prefix[i] = prefix[i - 1] + sorted_nums[i]
            if prefix[i] > 0:
                count += 1
        return count
        
        