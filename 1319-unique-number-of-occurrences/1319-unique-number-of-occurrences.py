class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        numToCount = {}
        for num in arr:
            numToCount[num] = numToCount.get(num, 0) + 1
        
        # Get all frequency values
        frequencies = list(numToCount.values())
        
        # Use a set to check if all frequencies are unique
        return len(frequencies) == len(set(frequencies))


        