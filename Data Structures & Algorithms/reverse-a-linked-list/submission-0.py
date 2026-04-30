class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        cur = head
        prev = None
        while (cur):
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        
        return prev