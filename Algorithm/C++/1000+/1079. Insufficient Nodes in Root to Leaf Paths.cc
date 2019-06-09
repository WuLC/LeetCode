/*
 * Created on Sun Jun 09 2019 18:6:27
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

 // recursive 
class Solution {
 public:
  TreeNode* sufficientSubset(TreeNode* root, int limit) {
    if (root->left == NULL && root->right == NULL) {
      if (root->val < limit)
        return NULL;
      else
        return root;
    }
    if (root->left)
      root->left = sufficientSubset(root->left, limit - root->val);
    if (root->right)
      root->right = sufficientSubset(root->right, limit - root->val);
    if (root->left || root->right)
      return root;
    else
      return NULL;
  }
};