class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if not nums:
            return 0

        n = len(nums)
        up = down = 1

        # If the sequence goes up, we can extend the last down sequence.
        # If it goes down, we can extend the last up sequence.
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                up = down + 1
            elif nums[i] < nums[i - 1]:
                down = up + 1

        return max(up, down)