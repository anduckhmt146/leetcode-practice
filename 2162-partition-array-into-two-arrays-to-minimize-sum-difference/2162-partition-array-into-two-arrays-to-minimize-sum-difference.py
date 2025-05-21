from typing import List
from bisect import bisect_left

class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        from itertools import combinations

        n = len(nums) // 2
        left, right = nums[:n], nums[n:]
        total = sum(nums)

        # Generate all possible sums for each half
        def get_sums(arr):
            res = [[] for _ in range(n + 1)]
            for k in range(n + 1):
                for comb in combinations(arr, k):
                    res[k].append(sum(comb))
            return res

        left_sums = get_sums(left)
        right_sums = get_sums(right)

        min_diff = float('inf')

        for k in range(n + 1):
            left_list = left_sums[k]
            right_list = right_sums[n - k]
            right_list.sort()

            for l in left_list:
                target = total // 2 - l
                idx = bisect_left(right_list, target)

                # Try closest values in right_list
                for j in [idx - 1, idx]:
                    if 0 <= j < len(right_list):
                        r = right_list[j]
                        s1 = l + r
                        s2 = total - s1
                        min_diff = min(min_diff, abs(s1 - s2))

        return min_diff
