# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        data={}
        while headA:
            data[headA]=1
            headA=headA.next
        while headB:
            if data.get(headB):
                return headB
            headB=headB.next