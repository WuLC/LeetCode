/*
 * @lc app=leetcode id=404 lang=cpp
 *
 * [404] Sum of Left Leaves
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
    int sumOfLeftLeaves(TreeNode* root) {
        if (root == nullptr) return 0;
        return helper(root->left, true) + helper(root->right, false);
    }

private:
    int helper(TreeNode* root, bool isLeft) {
        if (root == nullptr) {
            return 0;
        }
        if (root->left == nullptr && root->right == nullptr && isLeft) {
            return root->val;
        }
        return helper(root->left, true) + helper(root->right, false);
    }
};
// @lc code=end

