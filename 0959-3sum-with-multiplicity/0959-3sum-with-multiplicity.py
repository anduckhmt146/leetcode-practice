from typing import List
from collections import Counter

class Solution:
    def threeSumMulti(self, nums: List[int], target: int) -> int:
        MOD = 10**9 + 7
        count = 0
        freq = Counter(nums)
        nums = sorted(freq)  # unique values sorted

        for i in range(len(nums)):
            x = nums[i]
            for j in range(i, len(nums)):
                y = nums[j]
                z = target - x - y
                if z < y:
                    continue
                if z not in freq:
                    continue

                cx, cy, cz = freq[x], freq[y], freq[z]

                if x == y == z:
                    count += cx * (cx - 1) * (cx - 2) // 6
                elif x == y != z:
                    count += cx * (cx - 1) // 2 * cz
                elif x < y and y < z:
                    count += cx * cy * cz
                elif x != y and y == z:
                    count += cx * cy * (cy - 1) // 2

        return count % MOD
