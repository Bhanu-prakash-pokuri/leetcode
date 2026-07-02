class Solution(object):
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        stack = []
        t = [0]*n

        for l in logs:
            i, sta, cur = l.split(":")
            i, cur = int(i), int(cur)
            if sta == "start":
                stack.append([i, cur])

            else:
                x, y = stack.pop()
                time = cur - y + 1
                t[x] += time
                if stack:
                    x, _ = stack[-1]
                    t[x] -= time

        return t