class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = set()

        # Giong combination sum nhung khong co diem dung ma lay het
        def backtrack(start, path):
            result.add(tuple(path[:]))  # Add the current subset to the result
            for i in range(start, len(nums)):
                path.append(nums[i])
                # Can contain duplicate
                backtrack(i + 1, path)
                path.pop()

        backtrack(0, [])
        return [list(comb) for comb in result]
        