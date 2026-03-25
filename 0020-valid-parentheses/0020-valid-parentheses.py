class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for i in s:
            if i=="("or i=="{"or i=="[":
                stack.append(i)
            else:
                if not stack:
                    return False

                t=stack.pop()
                if i==")" and t!="(":
                    return False
                if i=="}" and t!="{":
                    return False
                if i=="]" and t!="[":
                    return False
        return len(stack)==0
                



        