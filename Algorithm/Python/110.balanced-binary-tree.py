#
# @lc app=leetcode id=110 lang=python
#
# [110] Balanced Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.helper(root) != -1
        
    def helper(self, node):
        if not node:
            return 0
        left = self.helper(node.left)
        right = self.helper(node.right)
        if left == -1 or right == -1 or abs(left - right) > 1:
            return -1
        return max(left, right) + 1
# @lc code=end

