"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        # return '#' when the node to the right of the node being checked is none, assume a perfect binary tree
        # use a queue to store the nodes
        # use a list to store the nodes in the same level

        queue = [root]

        while queue:
            for i in range(len(queue) - 1):
                queue[i].next = queue[i+1]
           
            for _ in range(len(queue)):
                current = queue.pop(0)
                if current and current.left:
                    queue.append(current.left)
                    queue.append(current.right)
        return root
