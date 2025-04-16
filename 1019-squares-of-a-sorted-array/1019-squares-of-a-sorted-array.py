class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        start, end = 0, len(nums) - 1
        highestSquare = len(nums) - 1
        result = [0] * len(nums)   

        while start <= end:
            startSquare = nums[start] ** 2
            endSquare = nums[end] ** 2

            if startSquare > endSquare:
                result[highestSquare] = startSquare
                start += 1
            else:
                result[highestSquare] = endSquare
                end -= 1

            highestSquare -= 1

        return result
            