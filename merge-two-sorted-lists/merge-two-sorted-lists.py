# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l3=ListNode(0)
        l4=l3
        while l1 and l2:
            if l1.val<=l2.val:
                l4.next=l1
                l1=l1.next
            else:
                l4.next=l2
                l2=l2.next
            l4=l4.next
        l4.next=l1 or l2
        return l3.next