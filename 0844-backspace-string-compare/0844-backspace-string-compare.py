class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        def rem(s):
            stack=[]
            for i in s:
                if i=="#" and stack:
                    stack.pop()
                elif i!="#":
                    stack.append(i)
            return stack
        return rem(s)==rem(t)

        