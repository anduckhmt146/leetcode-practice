class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nextNonDup = 0
        pE = 0

        while pE < len(nums):
            if pE < 2 or nums[pE] != nums[nextNonDup - 1] or nums[pE] != nums[nextNonDup - 2]:
                nums[nextNonDup] = nums[pE]
                nextNonDup += 1
            pE += 1

        return nextNonDup
        