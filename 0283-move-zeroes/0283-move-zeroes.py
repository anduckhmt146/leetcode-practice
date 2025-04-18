class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        nextNonZero = 0
        pE = 0
        while pE < len(nums):
            if nums[pE] != 0:
                nums[nextNonZero] = nums[pE]
                nextNonZero += 1
            pE += 1

        for i in range(nextNonZero, len(nums)):
            nums[i] = 0

        return nums
        