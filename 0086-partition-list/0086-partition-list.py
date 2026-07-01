# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        temp1=ListNode(0)
        temp2=ListNode(0)
        d1=temp1
        d2=temp2
        temp=head
        while(temp!=None):
            if temp.val<x:
                d1.next=temp
                d1=d1.next
            else:
                d2.next=temp
                d2=d2.next
            temp=temp.next
        d2.next=None
        d1.next=temp2.next
        return temp1.next
            

        