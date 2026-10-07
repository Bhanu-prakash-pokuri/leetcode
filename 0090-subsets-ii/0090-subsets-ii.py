class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        res=[]
        n=len(nums)
        def s(temp,i):
            if i>=n:
                p=temp[:]
                p.sort()
                if p not in res:
                    res.append(p)
                return
            temp.append(nums[i])
            s(temp,i+1)
            temp.pop()
            s(temp,i+1)
        s([],0)
        return res