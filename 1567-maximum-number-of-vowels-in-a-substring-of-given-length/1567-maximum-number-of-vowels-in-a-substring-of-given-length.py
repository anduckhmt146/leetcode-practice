class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        # Given a string, find the length of the longest substring in it with no more than K distinct characters.
        windowStart = 0
        maxLength = 0
        charFrequency = {} # store the frequence count of character
        vowelLetters = ['a', 'e', 'i', 'o', 'u']
        currVowels = 0  # Add this line to track current vowels


        # in the following loop we'll try to extend the range [windowStart, windowEnd]
        for windowEnd in range(0, len(s)):
            endChar = s[windowEnd]
            charFrequency[endChar] = charFrequency.get(endChar, 0) + 1

            if endChar in vowelLetters:
                currVowels += 1

            # shrink the window until we are left with k distinct characters 
            # in the charFrequency dictionary
            if windowEnd >= k:
                startChar = s[windowStart]
                charFrequency[startChar] -= 1

                if startChar in vowelLetters:
                    currVowels -= 1
            
                if charFrequency[startChar] == 0:
                    del charFrequency[startChar]
                windowStart += 1

            maxLength = max(maxLength, currVowels)

        return maxLength
        