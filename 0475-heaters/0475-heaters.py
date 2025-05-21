from typing import List
import bisect

class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        radius = 0

        for house in houses:
            # Find the position to insert the house in the sorted heaters list
            index = bisect.bisect_left(heaters, house)

            # Calculate distances to the nearest heater on the left and right
            left_dist = float('inf') if index == 0 else house - heaters[index - 1]
            right_dist = float('inf') if index == len(heaters) else heaters[index] - house

            # The nearest heater distance for this house
            nearest = min(left_dist, right_dist)

            # Update the required radius to cover all houses
            radius = max(radius, nearest)

        return radius
