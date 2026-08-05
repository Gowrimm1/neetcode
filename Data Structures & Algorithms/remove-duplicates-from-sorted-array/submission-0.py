class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        hashset=set()
        k=0
        for n in nums:
            if n not in hashset:
                hashset.add(n)
                nums[k]=n
                k+=1
        return k