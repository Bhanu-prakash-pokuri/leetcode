# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        def reverse(curr):
            prev=None
            while(curr):
                next=curr.next
                curr.next=prev
                prev=curr
                curr=next
            return prev
        fast=slow=head
        while(fast and fast.next):
            slow=slow.next
            fast=fast.next.next
        rev=reverse(slow)
        while rev:
            if rev.val!=head.val:
                return False
            head=head.next
            rev=rev.next
        return True
        