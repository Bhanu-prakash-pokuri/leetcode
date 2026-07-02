class Solution(object):
    def minAddToMakeValid(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack=[]
        for i in s:
            if i=="(":
                stack.append(i)
            else:
                if not stack:
                    stack.append(i)
                    continue
                

                t=stack[-1]
                if i==")" and t=="(":
                    stack.pop()
                
                else:
                    stack.append(i)
        return len(stack)
        