class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k=0
        hashset=set()
        count=0
        for n in nums:
            if n not in hashset:
                hashset.add(n)
                nums[k]=n
                count=1
                k+=1
            else:
                if count<2:
                    hashset.add(n)
                    nums[k]=n
                    count+=1
                    k+=1
        return k
                

        