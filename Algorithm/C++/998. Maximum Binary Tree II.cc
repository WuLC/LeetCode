/*
 * Created on Tue Feb 26 2019 21:27:1
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

// recursive, always insert to the right subtree of the current root
// use new to allocate memory instead of TreeNode new_root{val}, cause the latter one 
// will destroy the memory when return
class Solution {
 public:
  TreeNode* insertIntoMaxTree(TreeNode* root, int val) {
    if (root == nullptr || root->val < val) {
      TreeNode* new_root = new TreeNode{val};
      new_root->left = root;
      return new_root;
    } else {
      root->right = insertIntoMaxTree(root->right, val);
      return root;
    }
  }
};