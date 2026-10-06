class Solution:
    def maxIceCream(self, costs: list[int], coins: int) -> int:
        costs.sort()
        count = 0
        for cost in costs:
            if cost > coins:
                break
            count += 1
            coins -= cost
        return count