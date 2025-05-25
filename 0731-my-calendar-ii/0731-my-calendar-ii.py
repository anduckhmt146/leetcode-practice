class MyCalendarTwo:

    def __init__(self):
        self.booked = []
        self.overlaps = []

    def book(self, start: int, end: int) -> bool:
        # Check if it would cause a triple booking
        for os, oe in self.overlaps:
            if start < oe and end > os:
                return False

        # Add overlaps with existing bookings into overlaps list
        for bs, be in self.booked:
            if start < be and end > bs:
                self.overlaps.append((max(start, bs), min(end, be)))

        # Add to booked list
        self.booked.append((start, end))
        return True
