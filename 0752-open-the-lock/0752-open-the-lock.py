class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if '0000' in deadends:
            return -1
        visited={'0000'}
        q=deque([('0000',0)])

        while q:
            number,steps=q.popleft()
            if number==target:
                return steps
            for i in range(4):
                digit=int(number[i])
                up=(digit+1)%10
                down=(digit-1)%10
                upn=number[:i]+str(up)+number[i+1:]
                dnn=number[:i]+str(down)+number[i+1:]
                if upn not in deadends and upn not in visited:
                    visited.add(upn)
                    q.append((upn,steps+1))
                if dnn not in deadends and dnn not in visited:
                    visited.add(dnn)
                    q.append((dnn,steps+1))
        return -1
