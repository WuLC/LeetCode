/*
 * Created on Tue May 01 2018 21:47:29
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

 // always traverse from end to  start in the last line
class Solution 
{
    public:
        vector<vector<int>> zigzagLevelOrder(TreeNode* root) 
        {
            vector<vector<int>> result;
            if (root == NULL) return result;
            vector<TreeNode*> curr = {root};
            int flag = 1;
            while(!curr.empty())
            {
                vector<TreeNode*> next;
                vector<int> tmp;
                for(int i=curr.size()-1; i>=0; i--)
                {
                    tmp.push_back(curr[i]->val);
                    if (flag == 1)
                    {
                        if(curr[i]->left) next.push_back(curr[i]->left);
                        if(curr[i]->right) next.push_back(curr[i]->right);
                    }
                    else
                    {
                        if(curr[i]->right) next.push_back(curr[i]->right);
                        if(curr[i]->left) next.push_back(curr[i]->left);
                    }
                }
                flag *= -1;
                result.push_back(tmp);
                curr = next;
            }
            return result;
        }
};