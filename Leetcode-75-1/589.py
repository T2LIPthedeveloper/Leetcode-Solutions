"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        # result storage ig?
        # there's an issue with storing the result in a single function during the recursion so...
        result = []
        self.recurse(root, result)
        return result

    def recurse(self, root, result):
        if root == None:
            return
        result.append(root.val)
        for child in root.children:
            self.recurse(child, result)