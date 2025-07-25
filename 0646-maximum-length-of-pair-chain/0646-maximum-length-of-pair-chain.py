from typing import List

class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        # Sort pairs by the second element (end of the pair)
        pairs.sort(key=lambda x: x[1])
        
        curr_end = float('-inf')
        count = 0
        
        for start, end in pairs:
            if start > curr_end:
                count += 1
                curr_end = end
        
        return count
