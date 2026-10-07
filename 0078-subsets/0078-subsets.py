class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        res=[]
        n=len(nums)
        def s(temp,i):
            if i>=n:
                res.append(list(temp))
                return
            temp.append(nums[i])
            s(temp,i+1)
            temp.pop()
            s(temp,i+1)
        s([],0)
        return res