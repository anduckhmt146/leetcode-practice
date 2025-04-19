class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        windowStart = 0
        maxLength = 0
        maxRepeatOneCount = 0  # Track count of 1's instead of 0's
        bitFrequency = {}
        
        # Try to extend the range [windowStart, windowEnd]
        for windowEnd in range(0, len(nums)):
            endBit = nums[windowEnd]
            bitFrequency[endBit] = bitFrequency.get(endBit, 0) + 1
            
            # Track the count of 1's as our maxRepeat count
            if endBit == 1:
                maxRepeatOneCount = max(maxRepeatOneCount, bitFrequency[1])
            
            # Current window size minus count of 1's gives us count of 0's
            # If count of 0's exceeds k, shrink window
            if (windowEnd - windowStart + 1 - maxRepeatOneCount) > 1:
                startBit = nums[windowStart]
                bitFrequency[startBit] -= 1
                windowStart += 1
            
            maxLength = max(maxLength, windowEnd - windowStart + 1)
        
        return maxLength - 1 if maxLength > 0 else maxLength
        