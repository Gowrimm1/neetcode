class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap={}
        freq=[[] for i in range(0,len(nums)+1)]
        res=[]
        for n in nums:
            hashmap[n]=1+hashmap.get(n,0)
        for key,value in hashmap.items():
            freq[value].append(key)
        for i in range(len(nums),0,-1):
            for j in freq[i]:
                res.append(j)
                if len(res)==k:
                    return res
        return 