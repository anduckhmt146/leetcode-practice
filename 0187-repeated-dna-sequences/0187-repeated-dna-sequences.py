class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        # If string length is less than 10, no possible repeats
        if len(s) < 10:
            return []
        
        result = set()  # Store repeated sequences
        window = s[0:10]  # Initial window
        seen = {window}  # Track all seen sequences
        
        # Slide the window from index 1 to end
        for i in range(1, len(s) - 9):
            # Slide window one position right
            window = s[i:i+10]
            
            # If we've seen this sequence before, it's a repeat
            if window in seen:
                result.add(window)
            # If not seen, add to seen set
            else:
                seen.add(window)
        
        return list(result)
            