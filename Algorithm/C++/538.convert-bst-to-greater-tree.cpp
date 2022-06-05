/*
 * @lc app=leetcode id=538 lang=cpp
 *
 * [538] Convert BST to Greater Tree
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
    TreeNode* convertBST(TreeNode* root) {
        currSum = 0;
        dfs(root);
        return root;
    }

private:
    void dfs(TreeNode* root) {
        if (root == nullptr) return;
        dfs(root->right);
        currSum += root->val;
        root->val = currSum;
        dfs(root->left);
    }
    int currSum = 0;
};
// @lc code=end

