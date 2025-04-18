class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        freqMap = {}
        count = 0
        
        for num in nums:
            complement = k - num
            
            # If we have the complement and haven't used it yet
            if complement in freqMap and freqMap[complement] > 0:
                count += 1
                freqMap[complement] -= 1  # Mark the complement as used
            else:
                # Add current number to frequency map
                freqMap[num] = freqMap.get(num, 0) + 1
                
        return count
        