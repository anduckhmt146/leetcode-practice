from collections import Counter
import heapq
from typing import List

class Solution:
    def frequencySort(self, s: str) -> str:
         # Count frequencies using Counter
        count = Counter(s)
         # Build a heap of the k most frequent elements
        heap = heapq.nlargest(len(s), count.items(), key=lambda x: x[1])
        return ''.join([item * freq for item, freq in heap])
        