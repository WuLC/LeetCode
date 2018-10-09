/*
 * Created on Tue Oct 09 2018 14:30:13
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

// refer to heap 
class CBTInserter {
public:
    vector<TreeNode*> tree;
    CBTInserter(TreeNode* root) {
      std::queue<TreeNode*> q;
      q.push(root);
      TreeNode* tmp;
      while(!q.empty()) {
        tmp = q.front();
        q.pop();
        tree.push_back(tmp);
        if (tmp->left != NULL) q.push(tmp->left);
        if (tmp->right != NULL) q.push(tmp->right);
      }
    }
    
    int insert(int v) {
      TreeNode* node = new TreeNode(v);
      tree.push_back(node);
      int n = tree.size()-1;
      if (n % 2 == 0) {
        tree[int((n-2)/2)]->right = node;
        return tree[int((n-2)/2)]->val;
      }
      else {
        tree[int((n-1)/2)]->left = node;
        return tree[int((n-1)/2)]->val;
      }
    }
    
    TreeNode* get_root() {
      return tree[0];
    }
};

/**
 * Your CBTInserter object will be instantiated and called as such:
 * CBTInserter obj = new CBTInserter(root);
 * int param_1 = obj.insert(v);
 * TreeNode* param_2 = obj.get_root();
 */