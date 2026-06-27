class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum=nums[0]
        cur=0
        for i in range(len(nums)):
            cur=max(nums[i],cur+nums[i])
            max_sum=max(max_sum,cur)
        return max_sum 