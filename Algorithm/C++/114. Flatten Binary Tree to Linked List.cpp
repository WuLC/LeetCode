/*
 * Created on Sat Apr 21 2018 0:7:34
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

 // move the left tree of each node to its right tree
class Solution 
{
    public:
        void flatten(TreeNode* root) 
        {
            TreeNode *tmp;
            while(root)
            {
                if(root->left)
                {
                    tmp = root->left;
                    while(tmp->right) tmp = tmp->right;
                    tmp->right = root->right;
                    root->right = root->left;
                    root->left = NULL;
                }
                root = root->right;
            }
        }
};
