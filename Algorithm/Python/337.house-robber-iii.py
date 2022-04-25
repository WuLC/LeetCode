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
        return max(self.helper(root))

        
    def helper(self, node):
        """
        return tuple of result indicating (rob, unrob)
        """
        if node is None:
            return 0, 0
        left_rob, left_unrob = self.helper(node.left)
        right_rob, right_unrob = self.helper(node.right)
        
        return (node.val + left_unrob + right_unrob, 
                max(left_rob, left_unrob) + max(right_rob, right_unrob))
     
# @lc code=end

