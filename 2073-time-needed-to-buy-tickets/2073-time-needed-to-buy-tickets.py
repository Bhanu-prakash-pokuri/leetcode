class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        n=len(tickets)
        v=tickets[k]
        t=0
        for i in range(n):
            if i<k:
                t+=min(tickets[i],v)
            elif i==k:
                t+=v
            else:
                if tickets[i]<v:
                    t+=tickets[i]
                else:
                    t+=v-1
        return t
