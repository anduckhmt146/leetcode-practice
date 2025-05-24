class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # Step 1: Record the last occurrence of each character
        last_index = {char: idx for idx, char in enumerate(s)}
        
        result = []
        start = 0
        end = 0
        
        # Step 2: Iterate through the string to find partitions
        for i, char in enumerate(s):
            end = max(end, last_index[char])
            if i == end:
                result.append(end - start + 1)
                start = i + 1
        
        return result