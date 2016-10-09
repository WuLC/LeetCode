# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-06-23 23:32:15
# @Last modified by:   WuLC
# @Last Modified time: 2016-06-23 23:32:33
# @Email: liangchaowu5@gmail.com

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root == None or (root.left == None and root.right==None):
            return root
        left = self.invertTree(root.left)
        right = self.invertTree(root.right)
        root.left = right
        root.right = left
        return root
        