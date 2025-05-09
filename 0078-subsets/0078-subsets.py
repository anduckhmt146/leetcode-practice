class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        # Giong combination sum nhung khong co diem dung ma lay het
        def backtrack(start, path):
            result.append(path[:])  # Add the current subset to the result
            for i in range(start, len(nums)):
                path.append(nums[i])
                # Do not contain duplicate
                backtrack(i + 1, path)
                path.pop()

        backtrack(0, [])
        return result
        