from typing import List
from collections import Counter

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counts1 = Counter(nums1)
        result = []
        
        for num in nums2:
            if counts1[num] > 0:
                result.append(num)
                counts1[num] -= 1
        
        return result
