from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        if total_sum % 2 != 0:
            return False  # Can't partition an odd sum into two equal parts

        target = total_sum // 2
        dp = set([0])  # Initialize with sum 0 possible

        for num in nums:
            next_dp = set()
            for t in dp:
                if t + num == target:
                    return True
                next_dp.add(t)
                next_dp.add(t + num)
            dp = next_dp

        return target in dp
