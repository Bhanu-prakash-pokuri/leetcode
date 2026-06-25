class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        c=0
        l=0
        dic={'a':0,'b':0,'c':0}
        for r in range(len(s)):
            dic[s[r]]+=1
            while dic['a']>0 and dic['b']>0 and dic['c']>0:
                c+=len(s)-r
                dic[s[l]]-=1
                l+=1
        return c


        