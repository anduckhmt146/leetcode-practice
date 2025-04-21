class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # Find i number is larger than i
        # O(NlogN)
        citations.sort()

        maxHIndex = 0
        for i in range(0, len(citations)):
            # For example [1, and 5 values] => 1 must be pass
            h = min(citations[i], len(citations) - i)
            maxHIndex = max(maxHIndex, h)
        
        return maxHIndex