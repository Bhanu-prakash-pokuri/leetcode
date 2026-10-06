class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort(key=lambda x:x[1])
        ans=0
        preEnd=intervals[0][1]
        for start,end in intervals[1:]:
            if start<preEnd:
                ans+=1
            else:
                preEnd=end
        return ans