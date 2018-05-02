/*
 * Created on Wed May 02 2018 10:12:29
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

 // stack, iterative method
 // pay attention that stack.pop() return nothing
class Solution 
{
    public:
        vector<int> inorderTraversal(TreeNode* root)
        {
            vector<int> result;
            stack<TreeNode*> tmp;
            TreeNode* curr = root;
            while(!tmp.empty() || curr!=NULL)
            {
                if(curr != NULL)
                {
                    tmp.push(curr);
                    curr = curr->left;
                }
                else
                {
                    curr = tmp.top();
                    tmp.pop();
                    result.push_back(curr->val);
                    curr = curr->right;
                }
            }
            return result;
        }
};