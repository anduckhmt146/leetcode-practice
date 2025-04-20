class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        nextNonTarget = 0
        pE = 0
        while pE < len(nums):
            if nums[pE] != val:
                nums[nextNonTarget] = nums[pE]
                nextNonTarget += 1
            pE += 1

        return nextNonTarget