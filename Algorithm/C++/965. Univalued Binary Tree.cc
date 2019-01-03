/*
 * Created on Thu Jan 03 2019 9:38:30
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */


//  Definition for a binary tree node.
struct TreeNode {
  int val;
  TreeNode *left;
  TreeNode *right;
  TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 };

class Solution {
 public:
  bool isUnivalTree(TreeNode* root) {
    if (root->left != NULL) {
      bool same_left = root->val == root->left->val && isUnivalTree(root->left);
      if (!same_left) return false;
    }

    if (root->right != NULL) {
      bool same_right = root->val == root->right->val && isUnivalTree(root->right);
      if (!same_right) return false;
    }    
    return true;
  }
};