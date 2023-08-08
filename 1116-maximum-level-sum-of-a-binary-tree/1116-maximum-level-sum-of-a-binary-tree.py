# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        q = [root]
        maxsum = float('-inf')
        level = 0
        maxlevel = level
        while q:
            levelsum = 0
            level += 1
            for i in range(len(q)):
                curr = q.pop(0)
                levelsum += curr.val
                if curr.left: q.append(curr.left)
                if curr.right: q.append(curr.right)
            if levelsum > maxsum:
                maxsum = levelsum
                maxlevel = level
        return maxlevel
            