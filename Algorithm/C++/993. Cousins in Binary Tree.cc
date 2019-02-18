/*
 * Created on Mon Feb 18 2019 8:55:55
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

// simple recursive

#include <vector>

using std::vector;


class Solution {
 public:
  bool isCousins(TreeNode* root, int x, int y) {
    if (root->val == x || root->val == y) return false;
    vector<int> record;
    dfs(root, x, y, 0, record);
    return record[0] != record[2] && record[1] == record[3];
  }

 private:
  void dfs(TreeNode* root, int x, int y, int depth, vector<int>& record) {
    if (record.size() == 4) return;
    if (root->left != nullptr) {
      if (root->left->val == x || root->left->val == y) {
        record.push_back(root->val);
        record.push_back(depth+1);
      }
      dfs(root->left, x, y, depth+1, record);
    }
    if (root->right != nullptr) {
      if (root->right->val == x || root->right->val == y) {
        record.push_back(root->val);
        record.push_back(depth+1);
      }
      dfs(root->right, x, y, depth+1, record);
    }
  }
};