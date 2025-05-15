from typing import List

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def can_ship(capacity):
            current = 0
            required_days = 1
            for weight in weights:
                if current + weight > capacity:
                    required_days += 1
                    current = 0
                current += weight
            return required_days <= days

        left, right = max(weights), sum(weights)

        while left < right:
            mid = (left + right) // 2
            if can_ship(mid):
                right = mid  # Try a smaller capacity
            else:
                left = mid + 1  # Need more capacity

        return left
