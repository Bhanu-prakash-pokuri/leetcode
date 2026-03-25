# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k==0 or head==None:
            return head
        curr=head
        l=1
        while(curr.next!=None):
            curr=curr.next
            l+=1
        k%=l
        
        if k==0:
            curr.next=None 
            return head
        curr.next=head
        curr=head
        for i in range(l-k-1):
            curr=curr.next
        newhead=curr.next
        curr.next=None
        return newhead    
        