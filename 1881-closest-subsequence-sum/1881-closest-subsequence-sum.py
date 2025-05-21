from typing import List
from bisect import bisect_left

class Solution:
    def minAbsDifference(self, nums: List[int], goal: int) -> int:
        from itertools import combinations

        def get_all_sums(arr):
            res = set()
            for k in range(len(arr) + 1):
                for comb in combinations(arr, k):
                    res.add(sum(comb))
            return sorted(res)

        n = len(nums)
        left = nums[:n // 2]
        right = nums[n // 2:]

        left_sums = get_all_sums(left)
        right_sums = get_all_sums(right)

        ans = float('inf')

        for s in left_sums:
            remain = goal - s
            idx = bisect_left(right_sums, remain)
            # Try closest candidates on the right
            for j in [idx - 1, idx]:
                if 0 <= j < len(right_sums):
                    total = s + right_sums[j]
                    ans = min(ans, abs(goal - total))

        return ans
