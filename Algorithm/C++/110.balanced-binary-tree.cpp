/*
 * @lc app=leetcode id=110 lang=cpp
 *
 * [110] Balanced Binary Tree
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

#include <cmath>

class Solution {
public:
    bool isBalanced(TreeNode* root) {
        return helper(root) != -1;
    }

private:
    int helper(TreeNode* root) {
        if (root == nullptr) return 0;
        int left = helper(root->left);
        int right = helper(root->right);
        if (left == -1 || right == -1 || std::abs(left - right) > 1) return -1;
        return std::max(left, right) + 1;
    }
};
// @lc code=end

