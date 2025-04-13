class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        windowStart = 0
        maxLength = 0
        maxRepeatLetterCount = 0
        charFrequency = {}
        
        # Try to extend the range [windowStart, windowEnd]
        for windowEnd in range(0, len(s)):
            endChar = s[windowEnd]
            charFrequency[endChar] = charFrequency.get(endChar, 0) + 1
            
            # *REVIEW THIS LINE*
            maxRepeatLetterCount = max(maxRepeatLetterCount, charFrequency[endChar])


            # current window size is from windowStart to windowEnd, overall we have a letter which is
            # repeating maxRepeatLetterCount times, this means we can have a window which has one letter
            # repeating maxRepeatLetterCount times and the remaining letters we should replace
            # if the remaining letters are more than k, it is the time to shrink the window as we
            # are not allowed to replace more than k letters
            if (windowEnd - windowStart + 1 - maxRepeatLetterCount) > k:
                startChar = s[windowStart]
                charFrequency[startChar] -= 1
                windowStart += 1
                
            maxLength = max(maxLength, windowEnd - windowStart + 1)
        
        return maxLength
        