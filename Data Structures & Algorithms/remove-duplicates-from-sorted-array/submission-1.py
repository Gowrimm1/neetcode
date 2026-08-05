class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k=0
        hashset=set()
        for n in nums:
            if n not in hashset:
                hashset.add(n)
                nums[k]=n
                k+=1
        return k