# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s1, s2 = [], []

        while l1:
            s1.append(l1)
            l1 = l1.next
        
        while l2:
            s2.append(l2)
            l2 = l2.next

        prev = None
        
        carry = 0
        while s1 or s2 or carry:
            node1 = s1.pop() if s1 else None
            node2 = s2.pop() if s2 else None

            num1 = node1.val if node1 else 0
            num2 = node2.val if node2 else 0

            total = num1 + num2 + carry
            carry = total // 10
            cur = total % 10

            node = ListNode(cur, prev)
            prev = node
        
        return prev
        
        