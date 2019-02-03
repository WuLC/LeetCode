/*
 * Created on Sun Feb 03 2019 18:31:43
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
// std::min can not compare empty string

#include <string>

using std::string;

class Solution {
 public:
  string smallestFromLeaf(TreeNode* root) {
    if (root == nullptr) return "";
    string left = smallestFromLeaf(root->left);
    string right = smallestFromLeaf(root->right);
    if (left.length() == 0) {
      return right + char(root->val + 97);
    } else if (right.length() == 0) {
      return left + char(root->val + 97);
    } else {
      return std::min(left, right) + char(root->val + 97);
    }
  }
};