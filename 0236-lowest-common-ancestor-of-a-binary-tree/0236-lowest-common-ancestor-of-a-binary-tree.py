# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None

        def search(root, p, q):
            if not root:
                return None
            if root == p or root == q:
                return root

            left = search(root.left, p, q)
            right = search(root.right, p, q)

            if not left and right:
                return right
            if not right and left : 
                return left
            if left and right:
                return root

      
        return  search(root, p, q)