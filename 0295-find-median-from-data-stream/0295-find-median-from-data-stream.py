import heapq

# IDEA: A max heap to store the lower half of the numbers.
# IDEA: A min heap to store the upper half of the numbers.

class MedianFinder:

    def __init__(self):
        self.low = []  # Max heap (inverted min heap)
        self.high = []  # Min heap

    def addNum(self, num: int) -> None:
        # Add to max heap (invert the value to simulate max heap)
        heapq.heappush(self.low, -num)

        # Make sure every number in low is <= every number in high
        heapq.heappush(self.high, -heapq.heappop(self.low))

        # Balance the sizes (low can have one more element than high)
        if len(self.low) < len(self.high):
            heapq.heappush(self.low, -heapq.heappop(self.high))

    def findMedian(self) -> float:
        if len(self.low) > len(self.high):
            return -self.low[0]
        return (-self.low[0] + self.high[0]) / 2.0

        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()