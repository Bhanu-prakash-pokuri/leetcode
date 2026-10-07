class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        res=[]
        n=len(nums)
        def s(temp,i):
            if i>=n:
                res.append(list(temp))
                return
            temp.append(nums[i])
            s(temp,i+1)
            temp.pop()
            while i+1<n and nums[i]==nums[i+1]:
                i+=1
            s(temp,i+1)
        nums.sort()
        s([],0)
        return res