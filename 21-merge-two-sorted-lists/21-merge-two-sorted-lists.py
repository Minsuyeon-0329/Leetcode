# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        list3=ListNode(0)
        MergeLists = list3
        while list1 and list2 : 
            if list1.val <= list2.val :
                MergeLists.next=list1
                list1=list1.next
            else:
                MergeLists.next=list2
                list2=list2.next
            MergeLists = MergeLists.next
        MergeLists.next = list1 or list2
        
        return list3.next