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

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # Sort the array to handle duplicates
        result = set()
        for pE in range(0, len(nums)):
            # because the first solution is contain this solution too
            if pE > 0 and nums[pE] == nums[pE - 1]:
                continue

            firstVal = nums[pE]
            resultTwoSum = self.twoSum(nums, pE + 1, len(nums) - 1, 0 - firstVal)
            for [secondVal, thirdVal] in resultTwoSum:
                result.add((firstVal, secondVal, thirdVal))

        return [list(triplet) for triplet in result]
        

        