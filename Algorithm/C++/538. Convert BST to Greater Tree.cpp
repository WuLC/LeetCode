/*
 * Created on Wed May 02 2018 10:15:12
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

 // stack, reversed inorder traverse
class Solution {
    public:
        TreeNode* convertBST(TreeNode* root) 
        {
            stack<TreeNode*> tmp;
            TreeNode* curr = root;
            int acc_sum = 0;
            while(!tmp.empty() || curr)
            {
                if(curr)
                {
                    tmp.push(curr);
                    curr = curr->right;
                }
                else
                {
                    curr = tmp.top();
                    tmp.pop();
                    curr->val += acc_sum;
                    acc_sum = curr->val;
                    curr = curr->left;
                }
            }
            return root;
        }
};