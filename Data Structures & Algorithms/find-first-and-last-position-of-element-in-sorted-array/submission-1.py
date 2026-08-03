class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums) - 1
        
        # Move 'l' right until it finds target
        while l <= r and nums[l] != target:
            l += 1
            
        # Move 'r' left until it finds target
        while l <= r and nums[r] != target:
            r -= 1
            
        # If both landed on the target, return [l, r]
        if l <= r:
            return [l, r]
            
        return [-1, -1]
        