class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        # Count frequencies using Counter
        count = Counter(words)
        # Build a heap of the k most frequent elements, and by lexicalgraphical order
        # -x[1] ensures higher frequency comes first.
        # x[0] ensures lexicographical order among words with the same frequency.
        heap = heapq.nsmallest(k, count.items(), key=lambda x: (-x[1], x[0]))
        return [item for item, freq in heap]