class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_profit=float('INF')
        max_profit=0
        for price in prices:
            if min_profit>price:
                min_profit=price
            elif price-min_profit>max_profit:
                max_profit=price-min_profit
        return max_profit
        