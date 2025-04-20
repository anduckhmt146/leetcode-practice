from collections import Counter
import math

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        numsCounter = Counter(nums)

        for key, value in numsCounter.items():
            if value > math.floor(len(nums) / 2):
                return key

        return -1