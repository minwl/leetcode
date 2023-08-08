# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.longest=0
        
        def dfs(node, prev, cnt):
            if node:
                self.longest = max(self.longest, cnt)
                
                if prev == 0:
                    dfs(node.left, 1, cnt+1)
                    dfs(node.right, 0, 1)
                else:
                    dfs(node.right, 0, cnt+1)
                    dfs(node.left, 1, 1)
            else:
                return None

        if root.left:
            dfs(root.left, 1, 1)
        if root.right:
            dfs(root.right, 0, 1)
        
        return self.longest

