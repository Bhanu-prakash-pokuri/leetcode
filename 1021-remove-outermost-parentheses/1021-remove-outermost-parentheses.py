class Solution(object):
    def removeOuterParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        a=""
        o=0
        for c in s:
            if c == '(' and o > 0: 
                a+=c
            if c == ')' and o > 1: 
                a+=c
            o += 1 if c == '(' else -1
        return a

        
        