/*
 * Created on Tue Mar 12 2019 9:3:0
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

#include <vector>

using std::vector;


class Solution {
 public:
  TreeNode* bstFromPreorder(vector<int>& preorder) {
    return dfs(preorder, 0, preorder.size());
  }

  TreeNode* dfs(vector<int>& preorder, int left, int right) {
    if (left==right) return nullptr;
    TreeNode* root = new TreeNode(preorder[left]);
    int r = left + 1;
    while (r < preorder.size() && preorder[r] < preorder[left]) r++;
    root->left = dfs(preorder, left+1, r);
    root->right = dfs(preorder, r, right);
    return root;
  }
};