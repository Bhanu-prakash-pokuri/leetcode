class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        # from collections import Counter
        # c=Counter(students)
        # n=len(sandwiches)
        # for s in sandwiches:
        #     if c[s]==0:
        #         break
        #     c[s]-=1
        #     n-=1
        # return n

        c = 0
        while students:
            if students[0] == sandwiches[0]:
                sandwiches.pop(0)
                students.pop(0)
                c = 0
            else:
                students.append(students.pop(0))
                c += 1
            if c == len(students):
                break
        return len(students)

        