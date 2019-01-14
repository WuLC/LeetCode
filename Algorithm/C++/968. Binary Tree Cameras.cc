/*
 * Created on Mon Jan 14 2019 10:8:12
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

// greedy dfs, each node has three states
// 0 means that the node has been monitored but has no camera on it
// 1 means that the node has been monitored and has camera on it
// 2 means that the node has not been monitored
// referer: https://leetcode.com/problems/binary-tree-cameras/discuss/211180/JavaC++Python-Greedy-DFS

class Solution {
 public:
  int minCameraCover(TreeNode* root) {
    result = 0;
    if (dfs(root) == 2) result++;
    return result;
      
  }

  int dfs(TreeNode* root) {
    if (root == NULL) return 0;
    int left = dfs(root->left), right = dfs(root->right);
    if (left == 2 || right == 2) {
      result++;
      return 1;
    }
    return left == 0 && right == 0? 2: 0;
  }

  private:
   int result;
};