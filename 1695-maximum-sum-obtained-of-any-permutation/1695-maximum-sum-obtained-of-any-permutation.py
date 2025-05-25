from typing import List

class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        freq = [0] * (n + 1)

        # Use prefix sums to count frequency of each index in requests
        for start, end in requests:
            freq[start] += 1
            if end + 1 < n:
                freq[end + 1] -= 1
        
        # Prefix sum to get the exact frequency for each index
        for i in range(1, n):
            freq[i] += freq[i - 1]
        
        freq.pop()  # remove the extra element used for prefix sum

        # Sort nums and freq in descending order
        nums.sort(reverse=True)
        freq.sort(reverse=True)

        # Calculate max sum by multiplying sorted nums and freq
        result = 0
        for f, num in zip(freq, nums):
            result = (result + f * num) % MOD

        return result
