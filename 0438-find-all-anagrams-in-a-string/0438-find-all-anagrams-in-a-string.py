from collections import defaultdict
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        a=defaultdict(int)
        for i in p:
            if i not in a:
                a[i]=1
            else:
                a[i]+=1

        b=defaultdict(int)
        t=len(p)
    
        l=[]
        
        
        for i in range(len(s)):
            b[s[i]]+=1
            
            
            if i>=t:
                left=s[i-t]
                if b[left]==1:
                    del b[left]
                else:
                    b[left]-=1
           
            
            if b==a:
                l.append(i-t+1)
        return l