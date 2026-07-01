# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        s=ListNode(0)
        b=ListNode(0)
        l=s
        y=b
        temp=head
        while(temp!=None):
            if temp.val<x:
                l.next=temp
                l=l.next
            else:
                y.next=temp
                y=y.next
            temp=temp.next
        l.next=b.next
        y.next=None
        return s.next
            

        