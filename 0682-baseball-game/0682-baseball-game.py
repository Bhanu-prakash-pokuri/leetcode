class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        n=0
        stack=[]
        for i in operations:
            if i=="+":
                t=stack.pop()
                nt=t+stack[-1]
                stack.append(t)
                stack.append(nt)
            elif i=="C":
                stack.pop()
                continue
            elif i=="D":
                t=stack[-1]
                t*=2
                stack.append(t)
            else:
                stack.append(int(i))
        n+=sum(stack)
        return n
        