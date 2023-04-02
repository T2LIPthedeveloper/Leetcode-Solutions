# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        #return true if root contains subtree with structure of subRoot else false
        #use recursion to check if root contains subRoot
        #if root is None, return false
        #if root is not None, check if root is equal to subRoot
        def isEqual(root, subRoot):
            if root is None and subRoot is None:
                return True
            if root is None or subRoot is None:
                return False
            if root.val != subRoot.val:
                return False
            return isEqual(root.left, subRoot.left) and isEqual(root.right, subRoot.right)
        
        if root is None:
            return False
        if isEqual(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    