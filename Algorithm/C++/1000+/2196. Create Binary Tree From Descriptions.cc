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
#include <unordered_map>

class Solution {
public:
    TreeNode* createBinaryTree(std::vector<std::vector<int>>& descriptions) {
        std::unordered_map<int, TreeNode*> record;
        std::unordered_map<int, int> child2parent;
        int parent, child;
        bool isLeft;
        for(auto d: descriptions) {
            parent = d[0];
            child = d[1];
            isLeft = d[2];
            if (record.find(parent) == record.end()) {
                record[parent] = new TreeNode(parent);
            }
            if (record.find(child) == record.end()) {
                record[child] = new TreeNode(child);
            }
            if (isLeft) {
                record[parent]->left = record[child];
            } else {
                record[parent]->right = record[child];
            }
            child2parent[child] = parent;
        }
        TreeNode* root = nullptr;
        for (auto d: descriptions) {
            if (child2parent.find(d[0]) == child2parent.end()) {
                root = record[d[0]];
                break;
            }
        }
        return root;
    }
};