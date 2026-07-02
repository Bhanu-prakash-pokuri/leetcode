class Solution(object):
    def buildArray(self, target, n):
        """
        :type target: List[int]
        :type n: int
        :rtype: List[str]
        """
        res=[]
        t=0
        for i in range(1,n+1):
            if t==len(target):
                break
            if target[t]==i:
                res.append("Push")
                t+=1
            else:
                res.append("Push")
                res.append("Pop")
        return res



        