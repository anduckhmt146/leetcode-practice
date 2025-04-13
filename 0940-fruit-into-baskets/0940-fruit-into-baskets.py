class Solution:
    # it is longest subtring without k character
    def totalFruit(self, fruits: List[int]) -> int:
        windowStart = 0
        maxLength = 0
        k = 2
        fruitFrequency = {}  # store the frequence count of fruit

        # in the following loop we'll try to extend the range [windowStart, windowEnd]
        for windowEnd in range(0, len(fruits)):
            typeOfEndFruit = fruits[windowEnd]
            fruitFrequency[typeOfEndFruit] = fruitFrequency.get(typeOfEndFruit, 0) + 1

            # shrink the window until we are left with k distinct characters 
            # in the fruitFrequency dictionary
            while len(fruitFrequency) > k:
                typeOfStartFruit = fruits[windowStart]
                fruitFrequency[typeOfStartFruit] -= 1
            
                if fruitFrequency[typeOfStartFruit] == 0:
                    del fruitFrequency[typeOfStartFruit]
                windowStart += 1

            maxLength = max(maxLength, windowEnd - windowStart + 1)

        return maxLength
        