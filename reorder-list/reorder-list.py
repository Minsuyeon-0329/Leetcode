# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return head
        slow,fast=head,head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        
        crnt=slow
        temp=None
        while crnt:
            a=crnt.next
            crnt.next=temp
            temp=crnt
            crnt=a
            
        first,second=head,temp
        while second.next:
            first.next,first=second,first.next
            second.next,second=first,second.next
        return head