/*
 * @lc app=leetcode id=257 lang=cpp
 *
 * [257] Binary Tree Paths
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
#include <vector>
#include <string>

class Solution {
public:
    std::vector<std::string> binaryTreePaths(TreeNode* root) {
        std::vector<std::string> result;
        std::string tmp;
        if (root == nullptr) {
            return result;
        }
        dfs(result, tmp, root);
        return result;
    }

private:
    void dfs(std::vector<std::string>& result, std::string tmp, TreeNode* node) {
        if (tmp.size() > 0) {
            tmp += "->";
        }
        tmp += std::to_string(node->val);
        if (node->left == nullptr && node->right == nullptr) {
            result.push_back(tmp);
        } else {
            if (node->left != nullptr) {
                dfs(result, tmp, node->left);
            }
            if (node->right != nullptr) {
                dfs(result, tmp, node->right);
            }
        }
    }
};
// @lc code=end

