class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counts1,counts2={},{}
        if len(s1)>len(s2):
            return False
        l=0
        for r in range(len(s1)):
            counts1[s1[r]]=1+counts1.get(s1[r],0)
            counts2[s2[r]]=1+counts2.get(s2[r],0)
        if counts1==counts2:
            return True
        for i in range(len(s1),len(s2)):
            incoming=s2[i]
            counts2[incoming]=1+counts2.get(incoming,0)
            outgoing=s2[l]
            counts2[outgoing]-=1
            if counts2[outgoing]==0:
                del counts2[outgoing]
            l+=1
            if counts2==counts1:
                return True
        return False
            