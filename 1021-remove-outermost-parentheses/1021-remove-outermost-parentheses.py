class Solution(object):
    def removeOuterParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        res, o = [], 0
        for c in s:
            if c == '(' and o > 0: res.append(c)
            if c == ')' and o > 1: res.append(c)
            o += 1 if c == '(' else -1
        return "".join(res)
        