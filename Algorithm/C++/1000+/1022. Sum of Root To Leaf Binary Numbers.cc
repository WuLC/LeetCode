/*
 * Created on Tue Apr 09 2019 10:26:14
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
class Solution {
 public:
  int sumRootToLeaf(TreeNode* root) {
    return dfs(root, 0);
  }
 private:
  int dfs(TreeNode* root, int curr) {
    if (root->left == nullptr && root->right == nullptr) {
      return curr * 2 + root->val;
    }
    int tmp = 0;
    if (root->left != nullptr) tmp += dfs(root->left, curr * 2 + root->val);
    if (root->right != nullptr) tmp += dfs(root->right, curr * 2 + root->val);
    return tmp;
  }
};