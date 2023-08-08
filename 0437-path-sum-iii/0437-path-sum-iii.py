# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:

        def countpath(curr, sum):
            if not curr:
                return 0
            count = 0
            if curr.val == sum:
                count += 1
            count += countpath(curr.left, sum-curr.val) + countpath(curr.right, sum-curr.val)
            return count
        
        if not root:
            return 0
        return self.pathSum(root.left, targetSum) + self.pathSum(root.right, targetSum) + countpath(root, targetSum)

            