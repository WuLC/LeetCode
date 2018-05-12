/*
 * Created on Sat May 12 2018 17:58:52
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

// dfs, compare the difference between the following two implementations
// do not use inference for parameter tmp
class Solution 
{
    public:
        vector<vector<int>> pathSum(TreeNode* root, int sum) 
        {
            vector<vector<int>> result;
            vector<int> tmp;
            helper(root, sum, tmp, result);
            return result;
        }
        
        void helper(TreeNode* root, int sum, vector<int>& tmp, vector<vector<int>>& result)
        {
            if(root == NULL) return;
            tmp.push_back(root->val);
            if(root->val == sum && root->left == NULL && root->right == NULL)
            {
                result.push_back(tmp);
            }
            else
            {
                helper(root->left, sum - root->val, tmp, result);
                helper(root->right, sum - root->val, tmp, result);
            }
        }
};

// use inference for parameter tmp
class Solution 
{
    public:
        vector<vector<int>> pathSum(TreeNode* root, int sum) 
        {
            vector<vector<int>> result;
            vector<int> tmp;
            helper(root, sum, tmp, result);
            return result;
        }
        
        void helper(TreeNode* root, int sum, vector<int>& tmp, vector<vector<int>>& result)
        {
            if(root == NULL) return;
            tmp.push_back(root->val);
            if(root->val == sum && root->left == NULL && root->right == NULL)
            {
                result.push_back(tmp);
            }
            else
            {
                helper(root->left, sum - root->val, tmp, result);
                helper(root->right, sum - root->val, tmp, result);
            }
            tmp.pop_back();
        }
};