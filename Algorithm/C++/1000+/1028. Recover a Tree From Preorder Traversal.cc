/*
 * Created on Mon Apr 15 2019 13:5:38
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


// stack, two pointers
#include <stack>
#include <string>

class Solution {
 public:
  TreeNode* recoverFromPreorder(std::string S) {
    int p1 = 0, p2 = 0, level = 0;
    std::stack<TreeNode*> nodes;
    while (p2 < S.size()) {
      level = 0;
      while (S[p1] == '-') {
        p1++;
        p2++;
        level++;
      }
      while (p2 < S.size() && S[p2] != '-') p2++;
      TreeNode* curr_node = new TreeNode(std::stoi(S.substr(p1, p2 - p1)));
      while (nodes.size() > level) nodes.pop();
      if (nodes.size() > 0) {
        if (nodes.top()->left == nullptr)
          nodes.top()->left = curr_node;
        else
          nodes.top()->right = curr_node;
      }
      nodes.push(curr_node);
      p1 = p2;
    }
    while (nodes.size() > 1) nodes.pop();
    return nodes.top();
  }
};
