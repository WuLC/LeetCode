/*
 * @lc app=leetcode id=113 lang=cpp
 *
 * [113] Path Sum II
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

class Solution {
public:
    std::vector<std::vector<int>> pathSum(TreeNode* root, int targetSum) {
       std::vector<std::vector<int>>  result;
       std::vector<int> tmp;
       dfs(result, tmp, root, targetSum);
       return result; 

    }

private:
    void dfs(std::vector<std::vector<int>>& result, std::vector<int> tmp, TreeNode* node, int target) {
        if (node == nullptr) return;
        tmp.push_back(node->val);
        if (node->left == nullptr && node->right == nullptr && target == node->val) {
            result.push_back(tmp);
            return;
        }
        if (node->left != nullptr) {
            dfs(result, tmp, node->left, target - node->val);
        }
        if (node->right != nullptr) {
            dfs(result, tmp, node->right, target - node->val);
        }
    }

};
// @lc code=end

