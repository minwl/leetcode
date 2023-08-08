# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False
        return self.subtree(root.left, root.right)
            
        
    def subtree(self, leftp, rightp):
        if leftp == None and rightp == None: return True
        elif leftp == None or rightp == None: return False
        if leftp.val != rightp.val : return False
        else: 
            return self.subtree(leftp.left, rightp.right) and self.subtree(leftp.right, rightp.left)
