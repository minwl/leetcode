# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        seq1 = []
        seq2 = []
        def leafseq(root, seq):
            curr = root
            if curr == None:
                return None
            if curr.left == None and curr.right == None:
                seq.append(curr.val)
            else:
                leafseq(curr.left, seq)
                leafseq(curr.right, seq)
            return seq

        return leafseq(root1, seq1) == leafseq(root2, seq2)

