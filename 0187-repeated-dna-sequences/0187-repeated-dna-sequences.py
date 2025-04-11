class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        # Use sets to track seen sequences and repeated sequences
        seen = set()
        repeated = set()
        
        # Iterate through all possible 10-letter sequences
        for i in range(len(s) - 9):
            # Get current 10-letter sequence
            curr_seq = s[i:i+10]
            
            # If we've seen this sequence before, add to repeated
            if curr_seq in seen:
                repeated.add(curr_seq)
            # Otherwise, add to seen
            else:
                seen.add(curr_seq)
        
        # Convert repeated set to list and return
        return list(repeated)
        