# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.res = 0
        def dfs(node, prevMax):
            if not node:
                return
            if node.val >= prevMax:
                prevMax = node.val
                print(node.val)
                self.res += 1
            dfs(node.left, prevMax)
            dfs(node.right,prevMax)
        dfs(root, -200)
        return self.res