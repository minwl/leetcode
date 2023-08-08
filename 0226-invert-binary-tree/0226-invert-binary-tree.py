# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None:
            return None
        else:
            self.invertTree(root.left)
            self.invertTree(root.right)
            return self.invert(root)

        
    def invert(self, node):
        dummy = TreeNode()
        dummy.left = node.right
        dummy.right = node.left
        node.left = dummy.left
        node.right = dummy.right
        dummy.left = dummy.right = None
        return node