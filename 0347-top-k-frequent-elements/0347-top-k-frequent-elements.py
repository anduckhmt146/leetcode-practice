from collections import Counter
import heapq
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Count frequencies using Counter
        count = Counter(nums)
         # Build a heap of the k most frequent elements
        heap = heapq.nlargest(k, count.items(), key=lambda x: x[1])
        return [item for item, freq in heap]
