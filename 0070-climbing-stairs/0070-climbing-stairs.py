class Solution:
    def climbStairs(self, n: int) -> int:
        m={}
        def climb(n):
            if n in m:
                return m[n]
            if n<=1:
                return 1
            if n==2:
                return 2
            m[n]=climb(n-1)+climb(n-2)
            return m[n]
        c=climb(n)
        return c
        