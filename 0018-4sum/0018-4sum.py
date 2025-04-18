class Solution:
    def twoSum(self, nums: List[int], start: int, end: int, target: int) -> List[int]:
        # O(N)
        numToIndex = {}
        result = []
        for pE in range(start, end + 1):
            currVal = nums[pE]

            if target - currVal in numToIndex:
                result.append([currVal, target - currVal])
            
            numToIndex[currVal] = pE

        return result

    def threeSum(self, nums: List[int], start: int, end: int, target: int) -> List[List[int]]:
        result = []
        for pE in range(start, end + 1):
            firstVal = nums[pE]
            resultTwoSum = self.twoSum(nums, pE + 1, len(nums) - 1, target - firstVal)
            for [secondVal, thirdVal] in resultTwoSum:
                result.append([firstVal, secondVal, thirdVal])

        return result

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()  # Sort the array to handle duplicates
        result = set()
        for pE in range(0, len(nums)):
            if pE > 0 and nums[pE] == nums[pE - 1]:
                continue
            firstVal = nums[pE]
            resultThreeSum = self.threeSum(nums, pE + 1, len(nums) - 1, target - firstVal)
            for [secondVal, thirdVal, fourVal] in resultThreeSum:
                result.add((firstVal, secondVal, thirdVal, fourVal))

        return [list(triplet) for triplet in result]


        