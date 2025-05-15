class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        start = bisect.bisect_left(nums, target)  # First occurrence (lower bound)
        end = bisect.bisect_right(nums, target)   # First after last occurrence (upper bound)
        return list(range(start, end))
        