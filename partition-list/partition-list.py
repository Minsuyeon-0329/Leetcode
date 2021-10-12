# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        before_List=ListNode(0)
        before=before_List
        after_List=ListNode(0)
        after=after_List
        
        crnt =head
        while crnt:
            if crnt.val < x:
                before.next=crnt
                before = before.next
                crnt=crnt.next
            else:
                after.next=crnt
                after=after.next
                crnt=crnt.next
        after.next=None
        before.next=after_List.next
        return before_List.next