class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
            
        left = 0
        product = 1
        count = 0
        
        for right in range(0, len(nums)):
            product *= nums[right]
            
            # Move left pointer until product is less than k
            while product >= k:
                product //= nums[left]
                left += 1
                
            # Number of new subarrays ending at right
            count += right - left + 1
            
        return count
        