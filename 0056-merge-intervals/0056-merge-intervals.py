class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res=[intervals[0]]
        for i in range(1,len(intervals)):
            curr=intervals[i]
            prev=res[-1]
            if curr[0]<=prev[1]:
                prev[1]=max(prev[1],curr[1])
            else:
                res.append(curr)
        return res