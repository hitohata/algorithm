# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        if n == 1:
            return None if head.next is None else head.next

        l = 0
        cap = []
        h = head

        while h:
            cap.append(h)
            h = h.next

        prev = cap[l - n - 1]
        nex = cap[l - n + 1] if n >= l else None

        prev.next = nex

        return head
