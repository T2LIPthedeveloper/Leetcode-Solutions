# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # left to right, level by level returned in an array
        # breadth first search would be needed here
        if root == None:
            return []
        result = []
        queue = [root]
        while queue:
            current_level = []
            for i in range(len(queue)):
                current = queue.pop(0)
                current_level.append(current.val)
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
            result.append(current_level)
        return result
                
                