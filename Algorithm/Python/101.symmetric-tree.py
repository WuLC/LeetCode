#
# @lc app=leetcode id=101 lang=python
#
# [101] Symmetric Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from logging import RootLogger


class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.helper(root.left, root.right)
    
    def helper(self, n1, n2):
        if n1 == None or n2 == None:
            return n1 == None and n2 == None
        if n1.val != n2.val:
            return False
        else:
            return self.helper(n1.left, n2.right) and self.helper(n1.right, n2.left)
        
# @lc code=end

