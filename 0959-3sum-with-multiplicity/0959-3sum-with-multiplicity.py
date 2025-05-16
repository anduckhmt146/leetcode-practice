from typing import List
from collections import Counter

class Solution:
    def twoSum(self, nums: List[int], start: int, end: int, target: int, freq: Counter) -> List[tuple]:
        seen = {}
        result = set()

        for i in range(start, end + 1):
            curr = nums[i]
            complement = target - curr
            pair = tuple(sorted((curr, complement)))

            if complement in seen:
                result.add(pair)
            seen[curr] = i

        # Include counts with each pair
        counted_results = []
        for a, b in result:
            if a == b:
                count = freq[a] * (freq[a] - 1) // 2
            else:
                count = freq[a] * freq[b]
            counted_results.append((a, b, count))

        return counted_results

    def threeSumMulti(self, nums: List[int], target: int) -> int:
        MOD = 10**9 + 7
        nums.sort()
        freq = Counter(nums)
        n = len(nums)
        count = 0

        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue  # Skip duplicates for first value

            firstVal = nums[i]
            rest_target = target - firstVal
            # Get unique (a, b, count) pairs from twoSum
            resultTwoSum = self.twoSum(nums, i + 1, n - 1, rest_target, freq)

            for secondVal, thirdVal, pairCount in resultTwoSum:
                # Ensure order and uniqueness: firstVal <= secondVal <= thirdVal
                triplet = tuple(sorted([firstVal, secondVal, thirdVal]))
                a, b, c = triplet

                # Count valid combinations depending on value equality
                if a == b == c:
                    count += freq[a] * (freq[a] - 1) * (freq[a] - 2) // 6
                elif a == b:
                    count += freq[a] * (freq[a] - 1) // 2 * freq[c]
                elif b == c:
                    count += freq[b] * (freq[b] - 1) // 2 * freq[a]
                elif a == c:
                    count += freq[a] * (freq[a] - 1) // 2 * freq[b]
                else:
                    count += freq[a] * freq[b] * freq[c]

        return count % MOD
