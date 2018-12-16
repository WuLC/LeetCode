/*
 * Created on Sun Dec 16 2018 15:5:50
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */


#include <vector>

using std::vector;

struct TreeNode {
  int val;
  TreeNode *left;
  TreeNode *right;
  TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

// check level by level
class Solution {
 public:
  bool isCompleteTree(TreeNode* root) {
    vector<TreeNode*> curr{root};
    bool missed = false;
    while(curr.size() > 0) {
      vector<TreeNode*> next;
      for(auto node : curr) {
        if ((missed && (node->left != NULL || node->right != NULL)) || (node->left == NULL && node->right != NULL)) {
          return false;
        }
        if (node->left)
          next.push_back(node->left);
        else
          missed = true;
        if (node->right)
          next.push_back(node->right);
        else
          missed = true;   
      }
      curr = next;
    }
    return true;
  }
};