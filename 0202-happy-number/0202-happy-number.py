class Solution:
    def isHappy(self, n: int) -> bool:
        
        if n==1 or n==7:
            return True
        elif n<10:
            return False
        else:
            s=0
            while n>0:
                m=n%10
                s+=m*m
                n=n//10
        return self.isHappy(s)

        