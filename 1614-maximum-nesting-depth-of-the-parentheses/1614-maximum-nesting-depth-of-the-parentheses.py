class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        c=0
        m=0
        for i in s:
            if i=="(":
                c+=1
            if m<c:
                m=c
            if i==")":
                c-=1
            else:
                continue
        return m
