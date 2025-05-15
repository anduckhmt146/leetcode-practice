from typing import List
import math

class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        def time_required(speed: int) -> float:
            time = 0.0
            for i in range(len(dist) - 1):
                time += math.ceil(dist[i] / speed)
            time += dist[-1] / speed
            return time

        left, right = 1, 10**7
        result = -1

        while left <= right:
            mid = (left + right) // 2
            if time_required(mid) <= hour:
                result = mid
                right = mid - 1
            else:
                left = mid + 1

        return result
