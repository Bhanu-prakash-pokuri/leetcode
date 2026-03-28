class Solution:
    def fractionAddition(self, expression: str) -> str:
        import re
        from fractions import Fraction
        p=re.findall(r'[+-]?\d+/\d+',expression)
        s=sum(map(Fraction,p),Fraction(0,1))
        return f"{s.numerator}/{s.denominator}"
        