/*
 * Created on Sun Apr 14 2019 15:30:16
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

// bottom up dfs
#include <vector>
#include <cstdlib>


class Solution {
 public:
  int maxAncestorDiff(TreeNode* root) {
    return dfs(root)[2];
  }

 private:
  std::vector<int> dfs(TreeNode* root) {
    int max_num = root->val, min_num = root->val, max_diff = 0;
    if (root->left != nullptr) {
      std::vector<int> left = dfs(root->left);
      min_num = std::min(min_num, left[0]);
      max_num = std::max(max_num, left[1]);
      max_diff = std::max(max_diff, left[2]);
    }
    if (root->right != nullptr) {
      std::vector<int> right = dfs(root->right);
      min_num = std::min(min_num, right[0]);
      max_num = std::max(max_num, right[1]);
      max_diff = std::max(max_diff, right[2]);      
    }
    max_diff = std::max(std::max(std::abs(min_num - root->val), std::abs(max_num - root->val)), max_diff);
    return std::vector<int>{min_num, max_num, max_diff};
  }
};