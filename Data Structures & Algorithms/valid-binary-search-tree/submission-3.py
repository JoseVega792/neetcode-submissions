# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def validate(self, node, maxVal:int, minVal:int) -> bool:
        if not node:
            return True
        if minVal >= node.val or maxVal <= node.val:
            return False
        return self.validate(node.left, node.val, minVal) and self.validate(node.right, maxVal, node.val)
    
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.validate(root, float('inf'), float('-inf'))