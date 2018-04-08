# -*- coding: utf-8 -*-
# Created on Sun Apr 08 2018 19:50:19
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# recursive

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if self.isZeroTree(root):
            return None
        root.left = self.pruneTree(root.left)
        root.right = self.pruneTree(root.right)
        return root
    
    def isZeroTree(self, root):
        if root == None:
            return True
        if root.val == 1:
            return False
        return self.isZeroTree(root.left) and self.isZeroTree(root.right)