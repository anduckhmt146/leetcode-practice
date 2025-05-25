from collections import defaultdict

class MyCalendarThree:

    def __init__(self):
        self.timeline = defaultdict(int)
        self.max_overlap = 0

    def book(self, startTime: int, endTime: int) -> int:
        self.timeline[startTime] += 1
        self.timeline[endTime] -= 1

        # Sort keys and compute current overlap
        active = 0
        for time in sorted(self.timeline):
            active += self.timeline[time]
            self.max_overlap = max(self.max_overlap, active)

        return self.max_overlap
