/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    bool isSymmetric(TreeNode* root) {
        if (root == nullptr) return true;
        else return subsymmetric(root->left, root->right);
    }
    bool subsymmetric(TreeNode* leftsub, TreeNode* rightsub){
        if (leftsub == nullptr and rightsub == nullptr) return true;
        else if (leftsub == nullptr or rightsub == nullptr) return false;
        if (leftsub -> val != rightsub->val) return false;   
        else return subsymmetric(leftsub->left, rightsub->right) and subsymmetric(leftsub->right, rightsub->left);
    }
};