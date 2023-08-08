# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root : return []
        q = [root]
        ans = []
        while q:
            level = []
            for i in range(len(q)):
                curr = q.pop(0)
                level.append(curr.val)
                if curr.left : q.append(curr.left)
                if curr.right :q.append(curr.right)
            ans.append(level[-1])
        return ans