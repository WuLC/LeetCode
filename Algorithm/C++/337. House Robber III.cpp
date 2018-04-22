/*
 * Created on Sun Apr 22 2018 20:38:21
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
 // dfs, return 2 values given a node, one represents the result when robbing the node, the other represents not robbing the node
 // return vector instead of array
class Solution 
{
    public:
        int rob(TreeNode* root) 
        {
            vector<int> nums = helper(root);
            return max(nums[0], nums[1]);
        }
    
        vector<int> helper(TreeNode* root)
        {
            vector<int> curr = {0, 0};
            if (root!=NULL)
            {
                vector<int> left = helper(root->left);
                vector<int> right = helper(root->right);
                curr[0] = root->val + left[1] + right[1];
                curr[1] = max(left[0], left[1]) + max(right[0], right[1]);
            }
            return curr;
        }
};