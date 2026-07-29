class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap={}
        for i,n in enumerate(nums):
            rem=target-n
            if rem in prevMap:
                return [prevMap[rem],i]
            prevMap[n]=i
        return 
