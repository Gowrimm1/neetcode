class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        curr_sum=0
        count=0
        prefix_sum={0:1}
        for n in nums:
            curr_sum+=n
            diff=curr_sum-k
            if diff in prefix_sum:
                count+=prefix_sum[diff]
            prefix_sum[curr_sum]=1+prefix_sum.get(curr_sum,0)
        return count