class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = []
        d = path.split("/")
        for dir in d:
            if dir == "." or not dir:
                continue
            elif dir == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(dir)
        return "/" + "/".join(stack)