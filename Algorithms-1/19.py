# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l = 0
        node = head
        while node.next:
            node = node.next
            l += 1
        l += 1
        if l == n:
            return head.next
        node = head
        for i in range(l-n-1):
            node = node.next
        node.next = node.next.next
        return head
        