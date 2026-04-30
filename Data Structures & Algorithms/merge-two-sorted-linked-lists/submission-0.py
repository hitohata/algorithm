# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = node = ListNode()

        while (list1 or list2):
            if list2 is None:
                node.next = list1
                list1t = list1.next
            elif list1 is None:
                node.next = list2
                list2 = list2.next
            else:
                v1, v2 = list1.val, list2.val

                if v1 >= v2:
                    node.next = list2
                    list2 = list2.next
                else:
                    node.next = list1
                    list1 = list1.next
            node = node.next
        
        return dummy.next
            