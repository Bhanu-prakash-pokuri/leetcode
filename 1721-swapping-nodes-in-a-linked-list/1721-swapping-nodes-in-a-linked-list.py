# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
	    first = slow = head
	    for i in range(1, k):
		    first = first.next
		
	    fast = first 
	    while fast.next:
		    slow = slow.next
		    fast = fast.next
	    first.val, slow.val = slow.val, first.val
	    return head
	    
        