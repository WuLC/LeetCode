/*
 * Created on Sat Jun 02 2018 21:27:38
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */


// traverse the tree level by level
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
 
class Solution 
{
    public:
        vector<int> largestValues(TreeNode* root) 
        {
            vector<int> result;
            if (root==NULL) return result;
            vector<TreeNode*> curr;
            curr.push_back(root);
            while(curr.size() > 0)
            {
                vector<TreeNode*> next;
                int tmp = curr[0]->val;
                for(int i=0; i < curr.size(); i++)
                {
                    if(curr[i]->left) next.push_back(curr[i]->left);
                    if(curr[i]->right) next.push_back(curr[i]->right);
                    tmp = std::max(tmp, curr[i]->val);
                }
                result.push_back(tmp);
                curr = next;
            }
            return result;
        }
};