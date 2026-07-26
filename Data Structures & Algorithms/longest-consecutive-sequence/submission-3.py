class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset=set(nums)
        longest_streak=0
        for n in nums:
            if n-1 not in numset:
                current_num=n
                current_streak=1
                while(current_num+1 in numset):
                    current_num+=1
                    current_streak+=1
                longest_streak=max(longest_streak,current_streak)
        return longest_streak