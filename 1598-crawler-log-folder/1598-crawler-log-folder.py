class Solution(object):
    def minOperations(self, logs):
        """
        :type logs: List[str]
        :rtype: int
        """
        c=0
        for i in logs:
            if i=="../":
                if c==0:
                    continue
                else:
                    c-=1
            elif i=="./":
                continue
            else:
                c+=1
        return c
        