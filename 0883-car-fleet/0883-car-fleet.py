class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Zip and sort by position
        cars = sorted(zip(position, speed), reverse=True)

        # The car closest to target is process first, and other cars will pass it
        times = [(target - pos) / spd for pos, spd in cars]

        # Count fleets
        fleets = 0
        curr_time = 0

        for time in times:
            if time > curr_time:
                fleets += 1
                curr_time = max(curr_time, time)

        return fleets
        