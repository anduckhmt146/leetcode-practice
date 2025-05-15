class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        # Set search boundaries
        left = 1
        right = min(time) * totalTrips  # worst-case upper bound
        
        # Binary search
        while left < right:
            mid = (left + right) // 2
            trips = sum(mid // t for t in time)
            
            if trips >= totalTrips:
                right = mid
            else:
                left = mid + 1
        
        return left
            