class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # Use a list to store the change in passengers at each location
        passenger_changes = [0] * 1001  # Locations range from 0 to 1000
        
        for num_passengers, start, end in trips:
            passenger_changes[start] += num_passengers
            passenger_changes[end] -= num_passengers
        
        current_passengers = 0
        for passengers in passenger_changes:
            current_passengers += passengers
            if current_passengers > capacity:
                return False
        
        return True