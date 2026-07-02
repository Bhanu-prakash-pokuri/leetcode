class Solution(object):
    def minAddToMakeValid(self, s):
        """
        :type s: str
        :rtype: int
        """
        # stack=[]
        # for i in s:
        #     if i=="(":
        #         stack.append(i)
        #     else:
        #         if not stack:
        #             stack.append(i)
        #             continue
                

        #         t=stack[-1]
        #         if i==")" and t=="(":
        #             stack.pop()
                
        #         else:
        #             stack.append(i)
        # return len(stack)
        

        open_count = 0   
        additions = 0    

        for ch in s:
            if ch == "(":
                open_count += 1
            else:  # ch == ')'
                if open_count > 0:
                    open_count -= 1
                else:
                    additions += 1

        return additions + open_count