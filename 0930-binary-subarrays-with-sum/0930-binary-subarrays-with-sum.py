class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def atmost(nums,goal):
            c=0
            l=0
            r=0
            s=0
            for l in range (len(nums)):
                s+=nums[l]
            
                while s>goal and r<=l:
                    s-=nums[r]
                    r+=1
                c+=l-r+1
            
            
            return c
        return atmost(nums,goal)-atmost(nums,goal-1)

        