class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashmap={}
        for i,n in enumerate(numbers):
            rem=target-n
            if rem in hashmap:
                return [hashmap[rem]+1,i+1]
            hashmap[n]=i
        return 
