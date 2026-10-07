class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        res=[]
        def s(i,temp,k):
            if k==0:
                res.append(temp[:])
                return
            if i>n:
                return
            temp.append(i)
            s(i+1,temp,k-1)
            temp.pop()
            s(i+1,temp,k)
        s(1,[],k)
        return res

