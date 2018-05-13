/*
 * Created on Sun May 13 2018 15:6:52
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

 // recursive, decide whether the current root is included
class Solution 
{
    public:
        int pathSum(TreeNode* root, int sum) 
        {
            if (root== NULL) return 0;
            else return pathSum(root->left, sum) + pathSum(root->right, sum) + withRoot(root, sum);
        }
        int withRoot(TreeNode* root, int sum)
        {
            if(root == NULL) return 0;
            if(sum == root->val) return 1 + withRoot(root->left, 0) + withRoot(root->right, 0);
            return withRoot(root->left, sum - root->val) + withRoot(root->right, sum - root->val);
        }
};