class DinnerPlates:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.stacks = []
        self.available = []

    def push(self, val: int) -> None:
        while self.available and (
            self.available[0] >= len(self.stacks) or
            len(self.stacks[self.available[0]]) == self.capacity
        ):
            heappop(self.available)

        if not self.available:
            self.stacks.append([])
            heappush(self.available, len(self.stacks) - 1)

        idx = heappop(self.available)
        self.stacks[idx].append(val)

        if len(self.stacks[idx]) < self.capacity:
            heappush(self.available, idx)
        
    def pop(self) -> int:
        while self.stacks and not self.stacks[-1]:
            self.stacks.pop()

        if not self.stacks:
            return -1

        idx = len(self.stacks) - 1
        val = self.stacks[idx].pop()

        heappush(self.available, idx)

        while self.stacks and not self.stacks[-1]:
            self.stacks.pop()

        return val
        
    def popAtStack(self, index: int) -> int:
        if index >= len(self.stacks) or not self.stacks[index]:
            return -1
        val = self.stacks[index].pop()
        heappush(self.available, index)

        return val
        


# Your DinnerPlates object will be instantiated and called as such:
# obj = DinnerPlates(capacity)
# obj.push(val)
# param_2 = obj.pop()
# param_3 = obj.popAtStack(index)