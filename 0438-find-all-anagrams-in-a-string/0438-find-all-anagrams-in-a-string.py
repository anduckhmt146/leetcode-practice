class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # Edge cases
        if len(p) > len(s):
            return []
            
        # Initialize frequency maps
        pMap = {}
        windowMap = {}
        
        # Build frequency map for s1
        for char in p:
            pMap[char] = pMap.get(char, 0) + 1
            
        # Initialize sliding window with first len(s1) characters
        windowStart = 0

        # Result
        res = []
        
        # Try to extend the range [windowStart, windowEnd]
        for windowEnd in range(0, len(s)):
            # Add character to window frequency map
            endChar = s[windowEnd]
            windowMap[endChar] = windowMap.get(endChar, 0) + 1
            
            # If window size is larger than p length, shrink window
            if windowEnd >= len(p):
                startChar = s[windowStart]
                windowMap[startChar] -= 1
                
                # Remove character from map if count becomes 0
                if windowMap[startChar] == 0:
                    del windowMap[startChar]
                    
                windowStart += 1
            
            # Check if current window is a permutation
            if windowMap == pMap:
                res.append(windowEnd - len(p) + 1)
                
        return res
        