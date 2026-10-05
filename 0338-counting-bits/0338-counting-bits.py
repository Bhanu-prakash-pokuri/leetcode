class Solution:
    def countBits(self, n: int) -> list[int]:
        l=[0]*(n+1)
        for i in range(1,n+1):
            if i%2==0:
                l[i]=l[i//2]
            else:
                l[i]=l[i//2]+1
        return l
