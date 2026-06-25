from collections import defaultdict
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        dic=defaultdict(int)
        l=mx=0
        l1=[]
        for i in range(len(s)):
            dic[s[i]]=i
        for i in range(len(s)):
            mx=max(mx,dic[s[i]])
            if i==mx:
                l1.append(mx-l+1)
                l=i+1

        return l1




