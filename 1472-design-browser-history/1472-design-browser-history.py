class BrowserHistory:

    def __init__(self, homepage: str):
        self.hist=[]
        self.ford=[]
        self.hist.append(homepage)

    def visit(self, url: str) -> None:
        self.hist.append(url)
        self.ford=[]

    def back(self, steps: int) -> str:
        while steps>0 and len(self.hist)>1:
            self.ford.append(self.hist[-1])
            self.hist.pop()
            steps-=1
        return self.hist[-1]

    def forward(self, steps: int) -> str:
        while steps>0 and self.ford:
            self.hist.append(self.ford[-1])
            self.ford.pop()
            steps-=1
        return self.hist[-1]
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)