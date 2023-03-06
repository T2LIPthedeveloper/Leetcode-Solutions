# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # recursive solution
        previous = None #previous node is None
        while head != None:
            temp = head
            head = head.next
            temp.next = previous #initially None, meaning temp is the end of the list
            previous = temp
        return previous

#assumes usage of singly linked list, as prev pointer does not exist

