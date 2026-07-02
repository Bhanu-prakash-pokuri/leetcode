class StockSpanner(object):

    def __init__(self):
        self.monotone_stack=[]

    def next(self, price):
        """
        :type price: int
        :rtype: int
        """
        stack=self.monotone_stack
        curr_p,curr_s=price,1

        while stack and stack[-1][0]<=curr_p:
            prev_p,prev_s=stack.pop()
            curr_s+=prev_s
        stack.append((curr_p,curr_s))
        return curr_s
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)