/*
 * Created on Fri Jan 11 2019 19:46:24
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

// concise dfs
// referer: https://leetcode.com/problems/flip-binary-tree-to-match-preorder-traversal/discuss/214216/JavaC++Python-DFS-Solution

#include <vector>

using std::vector;

 struct TreeNode {
   int val;
   TreeNode *left;
   TreeNode *right;
   TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 };

class Solution {
 public:
  vector<int> flipMatchVoyage(TreeNode* root, vector<int>& voyage) {
    result.clear();
    idx = 0;
    return dfs(root, voyage)? result: vector<int>{-1};
  }

  bool dfs(TreeNode* root, vector<int>& voyage) {
    if (!root) return true;
    if (root->val != voyage[idx++]) return false;
    if (root->left != NULL && root->left->val != voyage[idx]){
      result.push_back(root->val);
      return dfs(root->right, voyage) && dfs(root->left, voyage);          
    } else {
      return dfs(root->left, voyage) && dfs(root->right, voyage); 
    }
  }

 private:
  vector<int> result;
  int idx;
};