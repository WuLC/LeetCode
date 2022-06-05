/*
 * @lc app=leetcode id=450 lang=cpp
 *
 * [450] Delete Node in a BST
 */

// @lc code=start
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

class Solution {
public:
    TreeNode* deleteNode(TreeNode* root, int key) {
       if (root == nullptr) {
           return root;
       }
       if (root->val > key) {
           root->left = deleteNode(root->left, key);
       } else if (root->val < key) {
           root->right = deleteNode(root->right, key);
       } else {
           if (root->left == nullptr) return root->right;
           if (root->right == nullptr) return root->left;
           int minVal = findMin(root->right);
           root->val = minVal;
           root->right = deleteNode(root->right, minVal);
       }
       return root;
    }
private:
    int findMin(TreeNode* root) {
        if (root->left == nullptr) {
            return root->val;
        }
        return findMin(root->left);
    }
};

// @lc code=end

