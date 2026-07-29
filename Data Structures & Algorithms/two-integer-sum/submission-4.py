class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevmap={}
        for i,n in enumerate(nums):
            rem=target-n
            if rem in prevmap:
                return [prevmap[rem],i]
            prevmap[n]=i
        return 