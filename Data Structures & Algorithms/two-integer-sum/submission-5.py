class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashset={}
        for i,n in enumerate(nums):
            rem=target-n
            if rem in hashset:
                return [hashset[rem],i]
            else:
                hashset[n]=i
        return 