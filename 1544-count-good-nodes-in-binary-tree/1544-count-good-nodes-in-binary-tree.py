# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        def dfs(curr, curmax):
            if not curr:
                return None
            if curr.val >= curmax:
                count[0] += 1
                curmax = curr.val
            dfs(curr.left, curmax)
            dfs(curr.right, curmax)
        

        count = [0]
        dfs(root, root.val)
        
        return count[0]
            


