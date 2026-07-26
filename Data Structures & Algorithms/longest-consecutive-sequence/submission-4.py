class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        streak=0

        for i,n in enumerate(nums):
            if n-1 in nums:
                continue
            current_num=n
            current_streak=1
            while(current_num+1 in nums):
                current_num+=1
                current_streak+=1
            streak=max(streak,current_streak)
        return streak
            