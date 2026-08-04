class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        x,y,z=target
        matched=set()
        for a,b,c in triplets:
            if a>x or b>y or c>z:
                continue
            if a==x:
                matched.add(0)
            if b==y:
                matched.add(1)
            if c==z:
                matched.add(2)
        return len(matched)==3