class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        
        def atmost(k):
            l=0
            a=0
            c=0
            for i in range(len(nums)):
                a+=nums[i]%2
                while a>k:
                    a-=nums[l]%2
                    l+=1
                c+=i-l+1
            return c
        count=atmost(k)-atmost(k-1)

        return count
            
        