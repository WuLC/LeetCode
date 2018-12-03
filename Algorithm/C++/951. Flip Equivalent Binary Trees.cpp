/*
 * Created on Mon Dec 03 2018 8:56:43
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

// simple recursive
class Solution {
 public:
  bool flipEquiv(TreeNode* root1, TreeNode* root2) {
    if (root1 == NULL && root2 == NULL)
      return true;
    else if (root1 == NULL || root2 == NULL)
      return false;
    else
      return root1->val == root2->val &&
             ((flipEquiv(root1->left, root2->left) && flipEquiv(root1->right, root2->right)) or
             (flipEquiv(root1->left, root2->right) && flipEquiv(root1->right, root2->left)));
  }
};