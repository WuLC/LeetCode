/*
 * Created on Fri Jan 25 2019 9:11:6
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

// recurvsive with postorder traverse
class Solution {
 public:
  int distributeCoins(TreeNode* root) {
    result = 0;
    traverse(root);
    return result;  
  }

  int traverse(TreeNode* root) {
    if (root == nullptr) return 0;
    int left = traverse(root->left), right = traverse(root->right);
    result += std::abs(left) + std::abs(right);
    return root->val + left + right - 1;
  }

 private:
  int result;
};