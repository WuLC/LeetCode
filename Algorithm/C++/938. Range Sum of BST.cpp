/*
 * Created on Mon Nov 12 2018 14:55:39
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
  int rangeSumBST(TreeNode* root, int L, int R) {
    if (root == NULL) return 0;
    if (root->val <= L) {
      if (root->val == L)
        return root->val + rangeSumBST(root->right, L, R);
      else
        return rangeSumBST(root->right, L, R);
    }
    else if (root->val >= R) {
      if (root->val == R)
        return root->val + rangeSumBST(root->left, L, R);
      else
        return rangeSumBST(root->left, L, R);
    }
    else {
      return root->val + rangeSumBST(root->left, L, root->val) + rangeSumBST(root->right, root->val, R);
    }
  }
}; 