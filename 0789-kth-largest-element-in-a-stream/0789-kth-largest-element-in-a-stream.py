import heapq

# IDEA: K largest use min heap
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.min_heap = nums
        # Inplace
        heapq.heapify(self.min_heap)
        # Maintain only the k largest elements in the heap
        while len(self.min_heap) > k:
            heapq.heappop(self.min_heap)

    def add(self, val: int) -> int:
        # Push first
        heapq.heappush(self.min_heap, val)

        # If heap grows beyond k, remove the smallest
        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)

        # The root is the k-th largest
        return self.min_heap[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)