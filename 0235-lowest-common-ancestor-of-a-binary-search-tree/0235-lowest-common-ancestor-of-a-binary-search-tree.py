# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        parentval = root.val
        pval= p.val
        qval = q.val
        #case 1: self tree
        if pval == parentval :
            return p
        if qval == parentval :
            return q
        #case 2 : different subtree
        if pval< parentval and parentval < qval :
            return root
        if qval < parentval and parentval < pval:
            return root
        #case 3: same subtree
        if pval < parentval and qval < parentval:
            return self.lowestCommonAncestor(root.left, p, q)
        if qval > parentval and pval > parentval:
            return self.lowestCommonAncestor(root.right, p, q)
