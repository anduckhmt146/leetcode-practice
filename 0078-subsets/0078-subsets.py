class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)

        def backtrack(index, path):
            if index == n:
                res.append(path[:])
                return

            backtrack(index + 1, path + [nums[index]])
            backtrack(index + 1, path)

        backtrack(0, [])
        return res