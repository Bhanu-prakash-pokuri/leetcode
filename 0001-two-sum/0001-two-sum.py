class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        from collections import defaultdict
        a=defaultdict(int)
        for i in range(len(nums)):
            b=target-nums[i]
            if b in a:
                return a[b],i
            a[nums[i]]=i
        
        return
        