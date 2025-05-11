class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        next_greater = {}
        
        for num in nums2:
            while stack and num > stack[-1]:
                prev_num = stack.pop()
                next_greater[prev_num] = num
            stack.append(num)
        
        # For elements that don't have a next greater element
        # We add all nums2 to stack, and use next_greater as a hash
        for num in stack:
            next_greater[num] = -1
        
        return [next_greater[num] for num in nums1]
        