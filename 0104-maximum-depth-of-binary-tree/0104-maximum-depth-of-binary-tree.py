# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        curr = root
        maxdep = 1
        maxdep += max(self.maxDepth(curr.left), self.maxDepth(curr.right))
        return maxdep

