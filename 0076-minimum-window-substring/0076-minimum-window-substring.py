class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Edge cases
        if not s or not t or len(s) < len(t):
            return ""
            
        # Initialize frequency maps
        targetMap = {}  # frequency map for string t
        windowMap = {}  # frequency map for current window
        
        # Build frequency map for target string
        for char in t:
            targetMap[char] = targetMap.get(char, 0) + 1
            
        # Initialize variables
        windowStart = 0
        minLength = float('inf')
        minStart = 0
        matched = 0  # count of characters matched with required frequency
        
        # Try to extend the range [windowStart, windowEnd]
        for windowEnd in range(len(s)):
            # Add current character to window frequency map
            endChar = s[windowEnd]
            windowMap[endChar] = windowMap.get(endChar, 0) + 1
            
            # If current character matches target frequency, increment matched count
            if endChar in targetMap and windowMap[endChar] == targetMap[endChar]:
                matched += 1
                
            # Try to shrink window when we have matched all characters
            while matched == len(targetMap):
                # Update minimum window size if current window is smaller
                windowLength = windowEnd - windowStart + 1
                if windowLength < minLength:
                    minLength = windowLength
                    minStart = windowStart
                
                # Remove character from start of window
                startChar = s[windowStart]
                windowMap[startChar] -= 1
                
                # If removed character was part of target and now frequency is less,
                # decrement matched count
                if startChar in targetMap and windowMap[startChar] < targetMap[startChar]:
                    matched -= 1
                    
                windowStart += 1
        
        # Return minimum window substring or empty string if not found
        return s[minStart:minStart + minLength] if minLength != float('inf') else ""
        