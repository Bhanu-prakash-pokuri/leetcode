class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        currmax=0
        currmin=0
        max_sum=float('-INF')
        min_sum=float('INF')
        n=len(nums)
        total=sum(nums)
        for i in range(n):
            currmax=max(nums[i],currmax+nums[i])
            max_sum=max(currmax,max_sum)
            

        for i in range(n):
            currmin=min(nums[i],currmin+nums[i])
            min_sum=min(currmin,min_sum)
            

        if max_sum<0:
            return max_sum
        return max(max_sum,total-min_sum)

        