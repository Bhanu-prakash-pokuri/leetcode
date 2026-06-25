from collections import defaultdict
class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        
        count=0
        
        def atmost(nums,k):
            c=0
            l=0
            dic=defaultdict(int)
            for i in range(len(nums)):
                dic[nums[i]]+=1
                while len(dic)>k:
                    dic[nums[l]]-=1
                    if dic[nums[l]]==0:
                        del dic[nums[l]]
                    l+=1
            
                c+=i-l+1
            return c
        count=atmost(nums,k)-atmost(nums,k-1)
        return count

        


        