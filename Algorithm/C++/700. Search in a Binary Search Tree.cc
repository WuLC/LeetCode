/*
 * Created on Thu Dec 20 2018 16:4:46
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */


struct TreeNode {
  int val;
  TreeNode *left;
  TreeNode *right;
  TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
 public:
  TreeNode* searchBST(TreeNode* root, int val) {
    if (root == NULL || root->val == val)
      return root;
    else if (root->val > val)
      return searchBST(root->left, val);
    else
      return searchBST(root->right, val);
  }
};