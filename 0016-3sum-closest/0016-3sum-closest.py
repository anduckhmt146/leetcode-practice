class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closestSum = float('inf')
        for pE in range(0, len(nums) - 2):
            left = pE + 1
            right = len(nums) - 1
            while (left < right):
                currSum = nums[pE] + nums[left] + nums[right]
                if abs(currSum - target) < abs(closestSum - target):
                    closestSum = currSum

                # Check with currSum
                if currSum < target:
                    left += 1
                elif currSum > target:
                    right -= 1
                else:
                    return currSum
        return closestSum
        