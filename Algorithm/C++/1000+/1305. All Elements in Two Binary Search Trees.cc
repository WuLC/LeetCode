/*
 * Created on Sun Jan 18 2020 10:20:44
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
#include <stack>

using std::vector;
using std::stack;

class Solution {
 public:
  vector<int> getAllElements(TreeNode* root1, TreeNode* root2) {
    stack<TreeNode> nodes1, node2;
    vector<int> result;
    TreeNode* curr1 = root2, curr2 = root2;
    reachLeftMost(nodes1, &curr1);
    reachLeftMost(nodes2, &curr2);
    while((curr1 || nodes1.size()>0) || (curr2 || nodes2.size()>0)) {
      bool pop1 = true;
      if (!curr1 && nodes1.size()>0) {
        curr1 = nodes1.top();
        nodes1.pop();
      }
      if (!curr2 && nodes2.size()>0) {
        curr2 = nodes2.top();
        nodes1.pop();
      }

    }
    
  }

 private:
  void reachLeftMost(stack<TreeNode>& unvisited, TreeNode* node) {
    if (node && node->left) {

    }
  }
};
