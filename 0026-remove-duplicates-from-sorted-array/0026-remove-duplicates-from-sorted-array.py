class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nextNonDup = 0
        n = len(nums)

        for i in range(n):
            if i == 0 or nums[i] != nums[nextNonDup - 1]:
                nums[nextNonDup] = nums[i]
                nextNonDup += 1

        return nextNonDup
