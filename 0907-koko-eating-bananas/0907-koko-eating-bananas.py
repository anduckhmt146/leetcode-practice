from typing import List
import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Define the search space for k
        left, right = 1, max(piles)

        while left < right:
            mid = (left + right) // 2
            # Calculate the total hours it would take at speed mid
            hours = sum(math.ceil(pile / mid) for pile in piles)

            if hours <= h:
                right = mid  # Try a smaller k
            else:
                left = mid + 1  # Increase k

        return left
