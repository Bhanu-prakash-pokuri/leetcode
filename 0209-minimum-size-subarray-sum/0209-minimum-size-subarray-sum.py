class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left=0
        win_sum=0
        min_len=float('inf')
        for i in range(len(nums)):
            win_sum+=nums[i]
            while (win_sum>=target):
                min_len=min(min_len,i-left+1)
                win_sum=win_sum-nums[left]
                left+=1
        if min_len!=float('inf'):
            return min_len
        return 0
        