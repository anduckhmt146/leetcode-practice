class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        # O(N^2)
        # res = []
        # for i in range(0, len(nums)):
        #     count = 0
        #     for j in range(0, len(nums)):
        #         if j != i and nums[j] < nums[i]:
        #             count += 1
        #     res.append(count)

        # return res


        # O(NlogN)
        sort_num = sorted(nums)
        numToIndex = {}

        # [1,2,2,3,8]
        for i, value in enumerate(sort_num):
            if value not in numToIndex:
                numToIndex[value] = i

        return [numToIndex[num] for num in nums]

        