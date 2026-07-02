class Solution(object):
    def scoreOfParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        a = 0
        d = 0

        for i in range(len(s)):
            if s[i] == "(":
                d += 1
            else:
                d -= 1
                if s[i - 1] == "(":
                    a += 2 ** d

        return a