# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # technically inorder traversal should provide a sorted arrayay so use that?
        array = []
        def inorder(root):
            if root == None:
                return
            inorder(root.left)
            array.append(root.val)
            inorder(root.right)
        inorder(root)

        #iterate through array to see if it's valid
        for i in range(len(array)-1):
            if array[i] >= array[i+1]:
                return False
        return True
    