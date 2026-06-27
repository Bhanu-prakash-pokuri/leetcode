class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum=float('-INF')
        cur=0
        for i in range(len(nums)):

            cur+=nums[i]
            max_sum=max(max_sum,cur)
            cur=0 if cur<0 else cur
        return max_sum 