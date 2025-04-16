class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nextNonDup = 1
        pE = 1
        while pE < len(nums):
            if nums[pE] != nums[nextNonDup - 1]:
                nums[nextNonDup] = nums[pE]
                nextNonDup += 1
            pE += 1

        return nextNonDup