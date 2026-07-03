class FreqStack:

    def __init__(self):
        self.s = []
        self.freq = defaultdict(int)

    def push(self, val: int) -> None:
        self.freq[val] += 1
        if self.freq[val] > len(self.s):
            self.s.append([val])
        else:
            self.s[self.freq[val]-1].append(val)
        

    def pop(self) -> int:
        val = self.s[-1].pop()
        if not self.s[-1]:
            self.s.pop()
        self.freq[val] -= 1
        return val


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()