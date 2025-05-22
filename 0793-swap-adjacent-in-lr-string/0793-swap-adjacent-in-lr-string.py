class Solution:
    def canTransform(self, start: str, result: str) -> bool:
        if start.replace("X", "") != result.replace("X", ""):
            return False

        i = j = 0
        while i < len(start) and j < len(result):
            # Skip Xs
            while i < len(start) and start[i] == 'X':
                i += 1
            while j < len(result) and result[j] == 'X':
                j += 1
            
            # If both reach end, they are transformable
            if i == len(start) and j == len(result):
                return True
            
            # If one string is done but not the other, it's invalid
            if i == len(start) or j == len(result):
                return False
            
            if start[i] != result[j]:
                return False

            # Check for invalid moves:
            if start[i] == 'L' and i < j:
                return False
            if start[i] == 'R' and i > j:
                return False

            i += 1
            j += 1
        
        return True
