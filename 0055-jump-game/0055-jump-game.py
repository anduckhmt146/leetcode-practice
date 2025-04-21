class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthest = 0
        for i in range(0, len(nums)):
            # Previous step can not read here
            if (i > farthest): 
                return False
            # Farthest jump at step i
            farthest = max(farthest, i + nums[i])
        
        return True
            