class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        streak=0
        for n in nums:
            if n-1 in nums:
                continue
            curr_num=n
            curr_streak=1
            while(curr_num+1 in nums):
                curr_num+=1
                curr_streak+=1
            streak=max(streak,curr_streak)
        return streak
            
                