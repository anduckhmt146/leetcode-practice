from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        # Create a frequency count of characters in s1
        s1_count = Counter(s1)
        
        # Create a frequency count of characters in the current window in s2
        window_count = Counter()
        
        # Initial window size is len(s1)
        for i in range(len(s1)):
            window_count[s2[i]] += 1
        
        # Check if the initial window is a permutation of s1
        if window_count == s1_count:
            return True
        
        # Slide the window across s2
        for i in range(len(s1), len(s2)):
            # Add the new character to the window
            window_count[s2[i]] += 1
            # Remove the leftmost character of the window
            window_count[s2[i - len(s1)]] -= 1
            
            # If the count becomes 0, remove the character from the window count to keep it clean
            if window_count[s2[i - len(s1)]] == 0:
                del window_count[s2[i - len(s1)]]
            
            # If the current window matches the s1_count, we found a permutation
            if window_count == s1_count:
                return True
        
        return False
