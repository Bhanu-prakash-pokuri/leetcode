class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        currmax=0
        currmin=0
        max_sum=float('-INF')
        min_sum=float('INF')
        n=len(nums)
        total=sum(nums)
        for i in range(n):
            currmax=nums[i] if nums[i]>currmax+nums[i] else currmax+nums[i]
            max_sum=currmax if currmax>max_sum else max_sum
            currmin=nums[i] if nums[i]<currmin+nums[i] else currmin+nums[i]
            min_sum=currmin if currmin<min_sum else min_sum
        if max_sum<0:
            return max_sum
        return max(max_sum,total-min_sum)

        