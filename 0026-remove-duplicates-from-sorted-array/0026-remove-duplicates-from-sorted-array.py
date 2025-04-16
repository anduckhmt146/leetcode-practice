class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nextNonDup = 0
        pE = 0

        while pE < len(nums):
            if pE == 0 or nums[nextNonDup - 1] != nums[pE]:
                nums[nextNonDup] = nums[pE]
                nextNonDup += 1
            pE += 1

        return nextNonDup
