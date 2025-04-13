from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Edge cases
        if len(s1) > len(s2):
            return False
            
        # Initialize frequency maps
        s1Map = {}
        windowMap = {}
        
        # Build frequency map for s1
        for char in s1:
            s1Map[char] = s1Map.get(char, 0) + 1
            
        # Initialize sliding window with first len(s1) characters
        windowStart = 0
        
        # Try to extend the range [windowStart, windowEnd]
        for windowEnd in range(len(s2)):
            # Add character to window frequency map
            endChar = s2[windowEnd]
            windowMap[endChar] = windowMap.get(endChar, 0) + 1
            
            # If window size is larger than s1 length, shrink window
            if windowEnd >= len(s1):
                startChar = s2[windowStart]
                windowMap[startChar] -= 1
                
                # Remove character from map if count becomes 0
                if windowMap[startChar] == 0:
                    del windowMap[startChar]
                    
                windowStart += 1
            
            # Check if current window is a permutation
            if windowMap == s1Map:
                return True
                
        return False
