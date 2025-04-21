class Solution:
    def jump(self, nums: List[int]) -> int:
        farthest = 0
        nextStep = 0
        count = 0
        # Final step do not need to jump
        for i in range(0, len(nums) - 1):
            # Previous step can not read here
            if (i > farthest): 
                return 0

            # Farthest jump at step i
            farthest = max(farthest, i + nums[i]) if i + nums[i] < len(nums) else len(nums) - 1

            # Jump in the largest step
            if i == nextStep:
                count += 1
                nextStep = farthest
        
        return count
        
        