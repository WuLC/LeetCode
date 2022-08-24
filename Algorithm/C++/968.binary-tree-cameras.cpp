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
    int minCameraCover(TreeNode* root) {
        result = 0;
        if (dfs(root) == 0) {
            result++;
        }
        return result;
    }

private:
    // three states:
    // 0: not cover
    // 1: has camera
    // 2: has no camera but is covered
    int dfs(TreeNode* node) {
        if (node == nullptr) {
            return 2;
        } 
        int left = dfs(node->left);
        int right = dfs(node->right);
        if (left == 0 || right == 0) {
            result++;
            return 1;
        }
        if (left == 1 || right == 1) {
            return 2;
        }
        return 0; // must be left == 2 && right == 2
    }

    int result;

};