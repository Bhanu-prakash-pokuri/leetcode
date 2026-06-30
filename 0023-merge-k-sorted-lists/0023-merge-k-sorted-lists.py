# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
         h = []
        
         for i in lists:
            while i:
                heapq.heappush(h, i.val)
                i = i.next
         dummy = ListNode(0)
         cur = dummy
         while h:
            cur.next = ListNode(heapq.heappop(h))
            cur = cur.next
         return dummy.next

        