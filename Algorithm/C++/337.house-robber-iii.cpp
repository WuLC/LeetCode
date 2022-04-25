/*
 * @lc app=leetcode id=337 lang=cpp
 *
 * [337] House Robber III
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

#include <utility>

using T = std::pair<int, int>;

class Solution {
public:
    int rob(TreeNode* root) {
        T result = helper(root);
        return std::max(result.first, result.second);
    }
private:
    // return the result of whether to rob the current node
    // the first one is to rob the current node
    T helper(TreeNode* node) {
        if (node == nullptr) {
            return std::make_pair(0, 0);
        }
        T left = helper(node->left);
        T right = helper(node->right);
        return std::make_pair(node->val + left.second + right.second,
            std::max(left.first, left.second) + std::max(right.first, right.second)
        );
    }
};
// @lc code=end

