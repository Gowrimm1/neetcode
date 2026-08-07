class Solution:
    def longestPalindrome(self, s: str) -> int:
        hashmap={}
        even_count=0
        length=0
        odd_count=0
        for ch in s:
            hashmap[ch]=1+hashmap.get(ch,0)
        for count in hashmap.values():
            if count%2==0:
                length+=count
            else:
                length+=count-1
                odd_count=True
        if odd_count:
            return length+1