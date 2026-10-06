class Solution:
    def numRescueBoats(self, p: list[int], limit: int) -> int:
        p.sort()
        c=0
        l, r=0, len(p)-1
        while l<=r:
            c+=1
            if p[l]+p[r]<=limit:
                l+=1
            r-=1
        return c