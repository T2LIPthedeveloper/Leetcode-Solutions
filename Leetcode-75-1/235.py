# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # lowest common ancestor is inclusive of current node.
        if p.val > q.val:
            p, q = q, p
        current = root
        while current:
            if current.val < p.val:
                current = current.right
            elif current.val > q.val:
                current = current.left
            else:
                return current