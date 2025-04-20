class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        original = nums[:]

        # Loop in the end
        for i in range(n - 1, -1, -1):
            nums[(i + k) % n] = original[i]

        return nums 
        