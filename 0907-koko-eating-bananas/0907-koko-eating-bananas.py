import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Greedy in range [1, max(piles)]
        left, right = 1, max(piles)

        def canEat(speed):
            count = 0
            for banana in piles:                    
                count += math.ceil(banana / speed)

            return count <= h

        while left <= right:
            mid = (left + right) // 2
            if canEat(mid):
                right = mid - 1
            else:
                left = mid + 1

        return left
            
