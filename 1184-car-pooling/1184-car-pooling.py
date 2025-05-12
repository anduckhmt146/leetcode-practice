from typing import List

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # Step 1: Use a difference array to track passenger changes at each location
        changes = [0] * 1001  # locations go from 0 to 1000

        for num_passengers, start, end in trips:
            changes[start] += num_passengers
            changes[end] -= num_passengers

        # Step 2: Sweep through the route and track the number of passengers
        current_passengers = 0
        for passengers in changes:
            current_passengers += passengers
            if current_passengers > capacity:
                return False

        return True
