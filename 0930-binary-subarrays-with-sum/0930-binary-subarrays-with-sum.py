class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def atmost(nums,goal):
            c=0
            l=0
            r=0
            s=0
            for r in range (len(nums)):
                s+=nums[r]
            
                while s>goal and l<=r:
                    s-=nums[l]
                    l+=1
                c+=r-l+1
            
            
            return c
        return atmost(nums,goal)-atmost(nums,goal-1)

        # result = 0
        # prefix_sum = 0
        # mp = {0: 1}
        # for num in nums:
        #     prefix_sum += num
        #     result += mp.get(prefix_sum - goal, 0)
        #     mp[prefix_sum] = mp.get(prefix_sum, 0) + 1
        # return result

        