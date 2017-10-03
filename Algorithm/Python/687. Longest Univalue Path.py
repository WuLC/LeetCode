# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2017-10-03 13:33:12
# @Last Modified by:   WuLC
# @Last Modified time: 2017-10-03 13:33:27

# recursive

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        count = 0
        if root.left and root.left.val == root.val:
            count += (1 + self.helper(root.left))
        if root.right and root.right.val == root.val:
            count += (1 + self.helper(root.right))
        return max(count, self.longestUnivaluePath(root.left), self.longestUnivaluePath(root.right))
    
    def helper(self, root):
        if root == None:
            return 0
        left, right = 0, 0
        if root.left and root.left.val == root.val:
            left = 1 + self.helper(root.left)
        if root.right and root.right.val == root.val:
            right = 1 + self.helper(root.right)
        return max(left, right)