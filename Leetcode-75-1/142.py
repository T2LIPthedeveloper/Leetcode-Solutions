# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # two pointer system
        # one pointer moves one node at a time
        # other pointer moves two nodes at a time
        # if they meet, then there is a cycle
        # if they do not meet, then there is no cycle
        # pos where cycle starts is not passed as a parameter of the function
        # return the node where the two pointers meet
        # if no cycle, return None

        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        else:
            return None
        while head != slow:
            head = head.next
            slow = slow.next
        return head
        
        # individual variable instantiation done for simplicity