/*
 * @lc app=leetcode id=1382 lang=cpp
 *
 * [1382] Balance a Binary Search Tree
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
    TreeNode* balanceBST(TreeNode* root) {
        std::vector<int> nums;
        traverse(root, nums);
        return construct(nums, 0, nums.size()-1);
    }

    void traverse(TreeNode* node, std::vector<int>& nums) {
        if (node == nullptr) {
            return;
        }
        traverse(node->left, nums);
        nums.push_back(node->val);
        traverse(node->right, nums);
    }

    TreeNode* construct(std::vector<int>& nums, int start, int end) {
        if (start > end) {
            return nullptr;
        }
        int mid = start + ((end-start)>>1);
        // std::shared_ptr<TreeNode> root = std::make_shared<TreeNode>(nums[mid]);
        TreeNode* root = new TreeNode(nums[mid]);
        root->left = construct(nums, start, mid-1);
        root->right = construct(nums, mid+1, end);
        return root;
    }
};
// @lc code=end

