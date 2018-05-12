/*
 * Created on Sat May 12 2018 18:8:42
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */


/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

 // simple recursive
class Solution 
{
    public:
        bool hasPathSum(TreeNode* root, int sum) 
        {
            if(root == NULL) return false;
            if(root->val == sum && root->left == NULL && root->right == NULL) return true;
            return hasPathSum(root->left, sum - root->val) || hasPathSum(root->right, sum - root->val);
        }
};