class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k<=1:
            return 0
        p=1
        l=0
        c=0
        for i in range(len(nums)):
            p*=nums[i]
            while p>=k:
                p=p//nums[l]
                l+=1
            c+=i-l+1
        return c

        

        