# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        mid = head
        end_finder = head
        while end_finder != None and end_finder.next != None:
            mid = mid.next
            end_finder = end_finder.next.next #works on the principle that a mid would be found within n/2 iterations
        return mid