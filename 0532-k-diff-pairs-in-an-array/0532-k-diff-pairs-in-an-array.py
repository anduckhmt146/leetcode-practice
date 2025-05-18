from typing import List

class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        if k < 0:
            return 0  # Absolute difference cannot be negative

        count = 0
        seen = {}
        
        for num in nums:
            seen[num] = seen.get(num, 0) + 1

        if k == 0:
            # Count elements with frequency >= 2
            for val in seen.values():
                if val > 1:
                    count += 1
        else:
            # Count unique pairs where num + k exists
            for num in seen:
                if num + k in seen:
                    count += 1

        return count
