# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        else:
            if root.left == None and root.right == None:
                return targetSum == root.val
            else:
                return self.hasPathSum(root.left, targetSum-root.val) or self.hasPathSum(root.right, targetSum-root.val)
            

    # def traverse(self, root):
    #     if not root:
    #         return False
    #     else:
    #         sum = root.val


            # right = root.val
            # left = root.val
            # if root.right:
            #     right += self.traverse(root.right)[0]
            # if root.left:
            #     left += self.traverse(root.left)[1]
            # return right,left


