#
# @lc app=leetcode id=337 lang=python
#
# [337] House Robber III
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(node):
            if node is None:
                return (0, 0)
            left = dfs(node.left)
            right = dfs(node.right)
            return (node.val + left[1] + right[1],
                    max(left) + max(right))
            
        return max(dfs(root))
        
# @lc code=end

