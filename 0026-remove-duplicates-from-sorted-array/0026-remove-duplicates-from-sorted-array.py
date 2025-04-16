class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nextNonDup = 0
        pE = 0
        while pE < len(nums):
            if pE == 0 or nums[pE] != nums[nextNonDup - 1]:
                nums[nextNonDup] = nums[pE]
                nextNonDup += 1
            pE += 1

        return nextNonDup