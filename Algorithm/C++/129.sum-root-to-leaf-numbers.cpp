/*
 * @lc app=leetcode id=129 lang=cpp
 *
 * [129] Sum Root to Leaf Numbers
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
    int sumNumbers(TreeNode* root) {
        result = 0;
        candidate.clear();
        dfs(root);
        return result;
    }

    void dfs(TreeNode* node) {
        if (node == nullptr) {
            return;
        }
        candidate.push_back(node->val);
        if (node->left == nullptr && node->right == nullptr) {
            int tmp = 0;
            for (int i = 0; i < candidate.size(); i++) {
                tmp = tmp*10 + candidate[i];
            }
            result += tmp;
        } else {
            dfs(node->left);
            dfs(node->right);
        }
        candidate.pop_back();
    }

private:
    int result;
    std::vector<int> candidate;
};

// @lc code=end

