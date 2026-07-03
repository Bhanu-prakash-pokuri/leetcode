class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        from collections import Counter
        c=Counter(students)
        n=len(sandwiches)
        for s in sandwiches:
            if c[s]==0:
                break
            c[s]-=1
            n-=1
        return n
        