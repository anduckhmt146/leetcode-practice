from typing import List
from collections import Counter

class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        count = Counter(ages)
        total = 0

        for ageA in count:
            for ageB in count:
                if ageB <= 0.5 * ageA + 7:
                    continue
                if ageB > ageA:
                    continue
                if ageB > 100 and ageA < 100:
                    continue
                if ageA == ageB:
                    total += count[ageA] * (count[ageA] - 1)
                else:
                    total += count[ageA] * count[ageB]
        
        return total
