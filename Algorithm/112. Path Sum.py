# -*- coding: utf-8 -*-
# @Author: LC
# @Date:   2016-07-04 10:05:59
# @Last modified by:   WuLC
# @Last Modified time: 2016-07-04 10:06:06
# @Email: liangchaowu5@gmail.com

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        return self.helper(root, sum, 0)
        
    def helper(self, root, sum ,count):
        if root == None:
            return False
        if sum == count+root.val and root.left == None and root.right == None:
            return True
        if self.helper(root.left, sum, count+root.val):
            return True
        elif self.helper(root.right, sum, count+root.val):
            return True
        else:
            return False