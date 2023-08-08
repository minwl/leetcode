# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.ans = True
        self.last = -inf
        def inOrder(root):
            if not root:
                return
            inOrder(root.left)
            if self.last >= root.val:
                self.ans = False
                return 
            else : 
                self.last = root.val
            inOrder(root.right)
        inOrder(root)
        return self.ans
        